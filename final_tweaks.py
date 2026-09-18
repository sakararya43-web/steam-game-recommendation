import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update overlay to blackish
old_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(20,0,0,0.1) 0%, rgba(10,0,0,0.65) 100%);
        }"""
new_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(5,10,15,0.4) 0%, rgba(0,0,0,0.9) 100%);
        }"""
content = content.replace(old_overlay, new_overlay)

# Update snow to white
old_snow = """        .snowflake {
            position: absolute; background: #ff0000; box-shadow: 0 0 5px rgba(255,0,0,0.8);
            animation: fall linear infinite; top: -10px;
        }"""
new_snow = """        .snowflake {
            position: absolute; background: #ffffff; box-shadow: 0 0 4px rgba(255,255,255,0.4);
            animation: fall linear infinite; top: -10px;
        }"""
content = content.replace(old_snow, new_snow)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

