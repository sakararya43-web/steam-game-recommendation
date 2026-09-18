import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix logo
content = re.sub(r'<div class="logo" onclick="location\.reload\(\)">', r'<div class="logo" style="cursor:pointer;" onclick="goHome()">', content)

# Inject Back button into nav-actions
back_button = """          <div class="nav-actions">
              <button id="backBtn" onclick="goHome()" style="background: rgba(0,0,0,0.5); border: 1px solid var(--primary); color: var(--primary); padding: 8px 16px; border-radius: 8px; font-weight: 600; cursor: pointer; margin-right: 15px; display: none; align-items: center; gap: 6px; transition: all 0.3s; backdrop-filter: blur(4px);">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                  Back
              </button>"""

content = re.sub(r'<div class="nav-actions">', back_button, content)

# Inject goHome function if it doesn't exist
if 'function goHome()' not in content:
    content = content.replace('let currentSteamId = "";', """let currentSteamId = "";

        function goHome() {
            document.getElementById('searchInput').value = '';
            document.getElementById('backBtn').style.display = 'none';
            fetchPopular();
        }""")

# Show back button when a search is done
if "document.getElementById('popularGames').innerHTML = '';" in content:
    content = content.replace("document.getElementById('popularGames').innerHTML = '';", "document.getElementById('popularGames').innerHTML = '';\n            document.getElementById('backBtn').style.display = 'flex';")

# Show back button when library is loaded
if "document.getElementById('sectionTitle').innerText = 'Your Steam Library';" in content:
    content = content.replace("document.getElementById('sectionTitle').innerText = 'Your Steam Library';", "document.getElementById('sectionTitle').innerText = 'Your Steam Library';\n            document.getElementById('backBtn').style.display = 'flex';")

# Also fix the login button to be RED!
content = content.replace("background: linear-gradient(135deg, #171a21, #2a475e);", "background: var(--btn-grad);")
content = content.replace("border: 1px solid #66c0f4;", "border: 1px solid var(--primary);")
content = content.replace("color: #66c0f4;", "color: white;")
content = content.replace("box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);", "box-shadow: 0 4px 10px rgba(255, 0, 60, 0.4);")
content = content.replace("background: linear-gradient(135deg, #2a475e, #66c0f4);", "background: linear-gradient(135deg, #ff003c 0%, #660000 100%);")
content = content.replace("box-shadow: 0 6px 15px rgba(102, 192, 244, 0.5);", "box-shadow: 0 6px 15px rgba(255, 0, 60, 0.5);")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

