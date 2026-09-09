from flask import Flask, send_from_directory, request, jsonify
import sys
import os

# Add src to path so we can import the recommender
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from recommender import GameRecommender
from steam_api import SteamAPI

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
app = Flask(__name__, static_url_path='/assets', static_folder=ASSETS_DIR)

# Initialize the recommender
print("Loading ML model...")
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model', 'model.pkl')
recommender = GameRecommender(model_path=MODEL_PATH)
steam_api = SteamAPI()

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/api/recommend', methods=['POST'])
def get_recommendations():
    data = request.json
    steam_id = data.get('steamId', '').strip()
    game_query = data.get('gameQuery', '').strip()
    app_id = data.get('appId')
    
    if not game_query:
        # Default fallback if empty
        game_query = recommender.df.iloc[0]['name']
        
    owned_games = []
    if steam_id:
        try:
            owned_games = steam_api.get_owned_games(steam_id)
            # Extract just the appids
            owned_games = [g['appid'] for g in owned_games] if owned_games else []
        except Exception as e:
            print(f"Error fetching steam games for {steam_id}: {e}")
            
    try:
        recommendations = recommender.recommend_games(game_query, app_id=app_id, top_n=10, owned_games=owned_games)
        
        # If the game wasn't found, recommendations might return a list of strings
        if recommendations and isinstance(recommendations[0], str):
            return jsonify({"error": recommendations[0]}), 404
            
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/library', methods=['GET'])
def get_library():
    steam_id = request.args.get('steamId', '').strip()
    if not steam_id:
        return jsonify({"error": "No Steam ID provided"}), 400
    try:
        owned_games = steam_api.get_owned_games(steam_id)
        # Limit to 20 for UI sake, and only games with playtime or names
        library = []
        if owned_games:
            # Sort by playtime_forever descending
            owned_games = sorted(owned_games, key=lambda x: x.get('playtime_forever', 0), reverse=True)
            for g in owned_games[:20]:
                library.append({
                    "name": g.get('name', f"App {g.get('appid')}"),
                    "appId": g.get('appid')
                })
        return jsonify({"library": library})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/popular', methods=['GET'])
def get_popular():
    try:
        # Just return the first 10 games from our dataset as 'popular'
        top_10 = recommender.df.head(10)
        res = []
        for _, row in top_10.iterrows():
            res.append({
                "name": row['name'],
                "appId": str(row['app_id']),
                "match": "Popular",
                "desc": str(row['description']),
                "sysReq": "OS: Win 10 | CPU: i5 | RAM: 8GB | GPU: GTX 1060"
            })
        return jsonify({"recommendations": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/game_details', methods=['GET'])
def get_game_details():
    app_id = request.args.get('appId')
    if not app_id:
        return jsonify({"error": "No App ID provided"}), 400
        
    try:
        import requests
        from concurrent.futures import ThreadPoolExecutor
        
        url_steam = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        url_spy = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
        
        def fetch_url(url):
            try:
                return requests.get(url, timeout=5).json()
            except Exception:
                return None
                
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_steam = executor.submit(fetch_url, url_steam)
            future_spy = executor.submit(fetch_url, url_spy)
            res_steam = future_steam.result()
            res_spy = future_spy.result()
            
        req_min = "System requirements not specified."
        desc = "No description available."
        devs = "Unknown"
        
        if res_steam and str(app_id) in res_steam and res_steam[str(app_id)]['success']:
            data = res_steam[str(app_id)]['data']
            sys_req = data.get('pc_requirements', {})
            if isinstance(sys_req, dict) and 'minimum' in sys_req:
                req_min = sys_req['minimum']
            desc = data.get('short_description', desc)
            devs = ", ".join(data.get('developers', []))
            
        rating = "No rating data"
        if res_spy:
            pos = res_spy.get('positive', 0)
            neg = res_spy.get('negative', 0)
            total = pos + neg
            rating = f"{int((pos/total)*100)}% Positive ({total:,} reviews)" if total > 0 else "No rating data"
            
        return jsonify({
            "sysReq": req_min,
            "desc": desc,
            "rating": rating,
            "devs": devs
        })
    except Exception as e:
        print(f"Error fetching game details: {e}")
        return jsonify({"error": "Failed to fetch details"}), 500

if __name__ == '__main__':
    print("Server running on http://127.0.0.1:5000")
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000)

