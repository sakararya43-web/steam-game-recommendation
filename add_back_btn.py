import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change logo onclick
content = content.replace('<div class="logo" onclick="location.reload()">', '<div class="logo" style="cursor:pointer;" onclick="goHome()">')

# 2. Add Back button to nav-actions
old_nav_actions = """          <div class="nav-actions">
              <span id="userStatus" style="color: #a0b6b8; font-size: 0.9rem; display: flex; align-items: center; gap: 6px; font-weight: 500;">"""

new_nav_actions = """          <div class="nav-actions">
              <button onclick="goHome()" style="background: transparent; border: 1px solid var(--primary); color: var(--primary); padding: 8px 16px; border-radius: 8px; font-weight: 600; cursor: pointer; margin-right: 15px; display: flex; align-items: center; gap: 6px; transition: all 0.3s;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                  Back
              </button>
              <span id="userStatus" style="color: #a0b6b8; font-size: 0.9rem; display: flex; align-items: center; gap: 6px; font-weight: 500;">"""
content = content.replace(old_nav_actions, new_nav_actions)

# 3. Add goHome() function
old_script_start = """        let currentSteamId = "";"""
new_script_start = """        let currentSteamId = "";

        function goHome() {
            document.getElementById('searchInput').value = '';
            fetchPopular();
        }"""
content = content.replace(old_script_start, new_script_start)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

