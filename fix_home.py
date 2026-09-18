import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix goHome function
content = re.sub(
    r'function goHome\(\)\s*\{\s*document\.getElementById\(\'searchInput\'\)\.value = \'\';\s*fetchPopular\(\);\s*\}',
    """function goHome() {
            if(document.getElementById('gameQuery')) document.getElementById('gameQuery').value = '';
            if(document.getElementById('backBtn')) document.getElementById('backBtn').style.display = 'none';
            fetchPopular();
        }""",
    content
)

# Add a Home button
home_btn = """<button id="homeBtn" onclick="goHome()" style="background: rgba(0,0,0,0.5); border: 1px solid var(--primary); color: var(--primary); padding: 8px 16px; border-radius: 8px; font-weight: 600; cursor: pointer; margin-right: 10px; display: flex; align-items: center; gap: 6px; transition: all 0.3s; backdrop-filter: blur(4px);">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                  Home
              </button>"""

if 'id="homeBtn"' not in content:
    content = content.replace('<div class="nav-actions">', f'<div class="nav-actions">\n              {home_btn}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

