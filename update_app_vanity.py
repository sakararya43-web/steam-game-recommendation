import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_library = """@app.route('/api/library', methods=['GET'])
def get_library():
    steam_id = request.args.get('steamId', '').strip()
    if not steam_id:
        return jsonify({"error": "No Steam ID provided"}), 400
    try:
        owned_games = steam_api.get_owned_games(steam_id)"""

new_library = """@app.route('/api/library', methods=['GET'])
def get_library():
    steam_id = request.args.get('steamId', '').strip()
    if not steam_id:
        return jsonify({"error": "No Steam ID provided"}), 400
    try:
        # If it's not a 17-digit number, try to resolve it as a custom URL/username
        if not (steam_id.isdigit() and len(steam_id) == 17):
            resolved_id = steam_api.resolve_vanity_url(steam_id)
            if resolved_id:
                steam_id = resolved_id
            
        owned_games = steam_api.get_owned_games(steam_id)"""

content = content.replace(old_library, new_library)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
