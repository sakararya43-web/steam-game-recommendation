import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update input placeholder
old_input = """<input type="text" id="steamIdInput" placeholder="Steam ID (e.g. 7656119...)">"""
new_input = """<input type="text" id="steamIdInput" placeholder="Steam ID or Custom Profile Name">"""
content = content.replace(old_input, new_input)

# Update error message
old_error = """else grid.innerHTML = `<p>No games found in this library. Note: Library must be public.</p>`;"""
new_error = """else grid.innerHTML = `<div style="text-align: center; max-width: 500px; margin: 40px auto; background: rgba(20,0,0,0.6); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,0,60,0.2);">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="var(--primary)" style="margin-bottom: 15px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
                    <h3 style="color: white; margin-bottom: 10px; font-size: 1.2rem;">Library is Private or Not Found</h3>
                    <p style="color: #a0b6b8; line-height: 1.6; font-size: 0.95rem;">If this is your account, you must set your Steam <strong>Game Details</strong> to Public.<br><br>Go to Steam > Edit Profile > Privacy Settings > Set "Game Details" to Public.</p>
                </div>`;"""
content = content.replace(old_error, new_error)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
