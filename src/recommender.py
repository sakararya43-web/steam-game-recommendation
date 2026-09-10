import joblib
import pandas as pd
import numpy as np
import requests

class GameRecommender:
    def __init__(self, model_path='../model/model.pkl'):
        model_data = joblib.load(model_path)
        self.tfidf = model_data['tfidf_vectorizer']
        self.cosine_sim = model_data['cosine_similarity']
        self.df = model_data['dataframe']
        self.indices = model_data['indices']
        self.tfidf_matrix = model_data['tfidf_matrix']
        
    def fetch_live_game_features(self, app_id):
        try:
            # Get app details from Steam API
            app_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
            app_res = requests.get(app_url).json()
            if not app_res or str(app_id) not in app_res or not app_res[str(app_id)]['success']:
                return None
                
            app_data = app_res[str(app_id)]['data']
            genres = [g['description'] for g in app_data.get('genres', [])]
            description = app_data.get('short_description', '')
            developer = ", ".join(app_data.get('developers', []))
            publisher = ", ".join(app_data.get('publishers', []))
            
            # Fetch tags from SteamSpy
            spy_url = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
            spy_res = requests.get(spy_url).json()
            tags = list(spy_res.get('tags', {}).keys()) if 'tags' in spy_res and isinstance(spy_res['tags'], dict) else []
            
            features = [
                ", ".join(genres),
                ", ".join(tags),
                str(description),
                str(developer),
                str(publisher)
            ]
            return " ".join(features)
        except Exception as e:
            print(f"Error fetching live data for {app_id}: {e}")
            return None

    def recommend_games(self, game_name, app_id=None, top_n=20, owned_games=None):
        idx = None
        game_vector = None
        target_info = None
        
        if game_name in self.indices:
            idx = self.indices[game_name]
            if isinstance(idx, pd.Series):
                idx = idx.iloc[0]
            game_vector = self.tfidf_matrix[idx]
            target_row = self.df.iloc[idx]
            app_id = str(target_row['app_id'])
            target_info = {
                "name": target_row['name'],
                "appId": app_id,
                "desc": str(target_row['description'])
            }
        else:
            matches = [name for name in self.indices.index if game_name.lower() in str(name).lower()]
            if matches:
                idx = self.indices[matches[0]]
                if isinstance(idx, pd.Series):
                    idx = idx.iloc[0]
                game_vector = self.tfidf_matrix[idx]
                target_row = self.df.iloc[idx]
                app_id = str(target_row['app_id'])
                game_name = target_row['name']
                target_info = {
                    "name": game_name,
                    "appId": app_id,
                    "desc": str(target_row['description'])
                }
            else:
                # If app_id not provided by frontend, try to search it!
                if not app_id:
                    try:
                        search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english&cc=US"
                        search_res = requests.get(search_url).json()
                        if search_res.get('total', 0) > 0 and search_res.get('items'):
                            app_id = str(search_res['items'][0]['id'])
                            game_name = search_res['items'][0]['name']  # Update name to official name
                    except Exception as e:
                        print(f"Error searching for {game_name}: {e}")
                
                if app_id:
                    # Live fetch using the resolved or provided app_id
                    combined_features = self.fetch_live_game_features(app_id)
                    if combined_features:
                        game_vector = self.tfidf.transform([combined_features])
                        target_info = {
                            "name": game_name,
                            "appId": app_id,
                            "desc": "Custom searched game not in database."
                        }
                    else:
                        return {"error": f"Game '{game_name}' found, but failed to fetch live details from Steam."}
                else:
                    return {"error": f"Game '{game_name}' not found on Steam. Try another search."}
            
        from sklearn.metrics.pairwise import cosine_similarity
        # Compute similarities against all games in our dataset
        sim_scores = cosine_similarity(game_vector, self.tfidf_matrix).flatten()
        
        # Boost sequels and related games
        target_base = game_name.lower().split(':')[0].split('-')[0].strip()
        if len(target_base) > 3:
            for j in range(len(sim_scores)):
                test_name = str(self.df.iloc[j]['name']).lower()
                if test_name.startswith(target_base) and test_name != game_name.lower():
                    sim_scores[j] += 0.35 # Massive boost for sequels
        
        # Add slight random noise to scores (0.0 to 0.04) to shuffle similar games (Diversity)
        noise = np.random.uniform(0, 0.04, size=sim_scores.shape)
        sim_scores += noise
        
        # Sort scores (highest to lowest)
        sim_indices = sim_scores.argsort()[::-1]
        
        recommendations = []
        owned_app_ids = set(owned_games) if owned_games else set()
        
        for i in sim_indices:
            # If we used a local index, skip the game itself
            if idx is not None and i == idx:
                continue
                
            score = sim_scores[i]
            game_app_id = self.df.iloc[i]['app_id']
            
            # Ensure we don't recommend the exact game we searched for (by app id)
            if game_app_id not in owned_app_ids and str(game_app_id) != str(app_id):
                game_row = self.df.iloc[i]
                
                # Cap match at 99%
                match_pct = min(int(score * 100), 99)
                
                recommendations.append({
                    "name": game_row['name'],
                    "appId": str(game_row['app_id']),
                    "match": f"{match_pct}%",
                    "desc": str(game_row['description']),
                    "sysReq": "OS: Win 10 | CPU: i5 | RAM: 8GB | GPU: GTX 1060"
                })
                if len(recommendations) == top_n:
                    break
                    
        return {"target": target_info, "recommendations": recommendations}

if __name__ == "__main__":
    recommender = GameRecommender()
    print("Testing recommendations for the first game in dataset...")
    test_game = recommender.df.iloc[0]['name']
    recs = recommender.recommend_games(test_game, top_n=10)
    print(f"\nRecommendations for {test_game}:")
    for game in recs:
        print(f"{game['name']}: {game['match']}")

