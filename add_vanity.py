import re

with open('src/steam_api.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add resolve_vanity_url method
new_method = """
    def resolve_vanity_url(self, vanity_name):
        url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
        params = {
            'key': self.api_key,
            'vanityurl': vanity_name
        }
        try:
            res = requests.get(url, params=params)
            if res.status_code == 200:
                data = res.json()
                if data.get('response', {}).get('success') == 1:
                    return data['response']['steamid']
        except Exception:
            pass
        return None
"""

content = content.replace("class SteamAPI:", "class SteamAPI:\n" + new_method)

with open('src/steam_api.py', 'w', encoding='utf-8') as f:
    f.write(content)
