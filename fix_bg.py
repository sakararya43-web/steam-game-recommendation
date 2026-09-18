import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove body::before
pattern = re.compile(r'\s*body::before\s*\{[^}]+\}', re.MULTILINE)
content = pattern.sub('', content)

# Bring z-indexes up so they render above body
content = content.replace("z-index: -3;", "z-index: 0;")
content = content.replace("z-index: -2;", "z-index: 1;")
content = content.replace("z-index: -1; pointer-events: none;", "z-index: 2; pointer-events: none;")

# Ensure content wrapper has higher z-index.
# I'll add a <div id="content-wrapper" style="position:relative; z-index: 10;"> around nav and main
old_body = """    <div id="snow-container"></div>
    <nav>"""
new_body = """    <div id="snow-container"></div>
    <div id="content-wrapper" style="position: relative; z-index: 10; display: flex; flex-direction: column; min-height: 100vh;">
    <nav>"""
content = content.replace(old_body, new_body)

old_script = """    <script>"""
new_script = """    </div>
    <script>"""
content = content.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

