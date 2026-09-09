import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SteamAPI:
    def __init__(self):
        self.api_key = os.getenv('STEAM_API_KEY')
        if not self.api_key:
            raise ValueError("STEAM_API_KEY not found in .env file")
            
    def get_owned_games(self, steam_id):
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'format': 'json',
            'include_appinfo': True
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'games' in data['response']:
                return data['response']['games']
            else:
                return []
        else:
            print(f"Error fetching games: {response.status_code}")
            return []

if __name__ == "__main__":
    try:
        steam = SteamAPI()
        print("Steam API Key successfully loaded.")
        # steam_id = 'YOUR_STEAM_ID'
        # games = steam.get_owned_games(steam_id)
        # print(f"Found {len(games)} games.")
    except Exception as e:
        print(f"Error: {e}")

