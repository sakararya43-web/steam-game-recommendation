import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

ping_route = """
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "awake"}), 200

"""

# Insert right after the index route
old_index = """@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')"""

new_index = old_index + ping_route

content = content.replace(old_index, new_index)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

