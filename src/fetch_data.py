import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def fetch_single_game(app_id):
    try:
        spy_url = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
        spy_res = requests.get(spy_url, timeout=5).json()
        if not spy_res or 'name' not in spy_res:
            return None
            
        name = spy_res.get('name', '')
        developer = spy_res.get('developer', '')
        publisher = spy_res.get('publisher', '')
        tags = list(spy_res.get('tags', {}).keys()) if 'tags' in spy_res and isinstance(spy_res['tags'], dict) else []
        
        return {
            'app_id': app_id,
            'name': name,
            'genres': "", # SteamSpy doesn't return genres list directly, but tags covers it
            'tags': ", ".join(tags),
            'description': f"A popular game by {developer}.", # Placeholder
            'developer': developer,
            'publisher': publisher
        }
    except Exception:
        return None

def fetch_games_data():
    print("Fetching top 2000 games list from SteamSpy API...")
    url = "https://steamspy.com/api.php?request=all&page=0"
    data = requests.get(url).json()
    
    url2 = "https://steamspy.com/api.php?request=all&page=1"
    data2 = requests.get(url2).json()
    
    data.update(data2)
    
    # data is a dict of appid -> game details. We want the ones with highest owners/ccu
    # The 'all' endpoint is already roughly sorted, but we can sort by ccu
    sorted_apps = sorted(data.values(), key=lambda x: x.get('ccu', 0), reverse=True)
    app_ids = [app['appid'] for app in sorted_apps[:2000]]
    
    print(f"Fetching details for {len(app_ids)} games concurrently...")
    
    games_list = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(fetch_single_game, app_ids)
        for res in results:
            if res:
                games_list.append(res)
                if len(games_list) % 25 == 0:
                    print(f"Downloaded {len(games_list)} games...")
                    
    df = pd.DataFrame(games_list)
    df.to_csv('../data/games.csv', index=False)
    print(f"Saved {len(df)} games to data/games.csv")

if __name__ == "__main__":
    fetch_games_data()

