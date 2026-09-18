import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix goHome function
old_gohome = """        function goHome() {
            document.getElementById('searchInput').value = '';
            document.getElementById('backBtn').style.display = 'none';
            fetchPopular();
        }"""
new_gohome = """        function goHome() {
            if(document.getElementById('gameQuery')) document.getElementById('gameQuery').value = '';
            if(document.getElementById('backBtn')) document.getElementById('backBtn').style.display = 'none';
            fetchPopular();
        }"""
content = content.replace(old_gohome, new_gohome)

# Inject into fetchRecommendations
if "document.getElementById('backBtn').style.display = 'flex';" not in content:
    content = content.replace("document.getElementById('gridTitle').innerText = `Recommendations for \"${query}\"`;", "document.getElementById('gridTitle').innerText = `Recommendations for \"${query}\"`;\n            document.getElementById('backBtn').style.display = 'flex';")

    # Inject into handleLogin
    content = content.replace('document.getElementById(\'gridTitle\').innerText = "Your Library";', 'document.getElementById(\'gridTitle\').innerText = "Your Library";\n            document.getElementById(\'backBtn\').style.display = \'flex\';')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

