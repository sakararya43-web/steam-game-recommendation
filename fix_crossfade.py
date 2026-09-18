import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_keyframes = """        @keyframes fadeCycle {
            0%, 15% { opacity: 1; }
            20%, 95% { opacity: 0; }
            100% { opacity: 1; }
        }"""
new_keyframes = """        @keyframes fadeCycle {
            0% { opacity: 0; }
            5% { opacity: 1; }
            20% { opacity: 1; }
            25% { opacity: 0; }
            100% { opacity: 0; }
        }"""
content = content.replace(old_keyframes, new_keyframes)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

