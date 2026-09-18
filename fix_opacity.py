import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the fade cycle fully opaque
old_keyframes = """        @keyframes fadeCycle {
            0%, 20% { opacity: 0.5; }
            25%, 95% { opacity: 0; }
            100% { opacity: 0.5; }
        }"""
new_keyframes = """        @keyframes fadeCycle {
            0%, 20% { opacity: 1; }
            25%, 95% { opacity: 0; }
            100% { opacity: 1; }
        }"""
content = content.replace(old_keyframes, new_keyframes)

# Make the dark overlay much lighter
old_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1;
            background: radial-gradient(circle at center, rgba(5,15,20,0.85) 0%, rgba(0,0,0,0.98) 100%);
        }"""
new_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(5,15,20,0.4) 0%, rgba(0,0,0,0.85) 100%);
        }"""
content = content.replace(old_overlay, new_overlay)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

