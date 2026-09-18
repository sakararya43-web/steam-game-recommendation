import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the modal massive for 1080p displays
old_modal_css = """        .modal {
            background: rgba(10, 30, 35, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 24px; width: 95%; max-width: 1200px;
            text-align: left; box-shadow: 0 30px 60px rgba(0,0,0,0.9), 0 0 40px rgba(0, 229, 255, 0.1); 
            position: relative; overflow: hidden; animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex; flex-direction: row; max-height: 85vh;
        }"""

new_modal_css = """        .modal {
            background: rgba(10, 30, 35, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 24px; width: 98%; max-width: 1800px; height: 92vh;
            text-align: left; box-shadow: 0 30px 60px rgba(0,0,0,0.9), 0 0 40px rgba(0, 229, 255, 0.1); 
            position: relative; overflow: hidden; animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex; flex-direction: row;
        }"""
content = content.replace(old_modal_css, new_modal_css)

# Adjust flex ratio so video is even wider (approaching 16:9 inside the modal)
content = content.replace("flex: 2; background: #000; position: relative;", "flex: 2.8; background: #000; position: relative;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

