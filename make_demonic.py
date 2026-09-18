import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS variables
old_root = """        :root {
            --bg-color: #050a0f;
            --surface: #0a1e23;
            --primary: #00e5ff;
            --secondary: #0055ff;
            --text-main: #f0f8ff;
            --text-muted: #8aa3a6;
            --glass-bg: rgba(10, 30, 35, 0.7);
            --glass-border: rgba(0, 229, 255, 0.15);
            --btn-grad: linear-gradient(135deg, #00e5ff 0%, #0055ff 100%);
        }"""
new_root = """        :root {
            --bg-color: #050000;
            --surface: #120000;
            --primary: #ff003c;
            --secondary: #8b0000;
            --text-main: #fff0f0;
            --text-muted: #a68a8a;
            --glass-bg: rgba(20, 0, 0, 0.85);
            --glass-border: rgba(255, 0, 60, 0.2);
            --btn-grad: linear-gradient(135deg, #ff003c 0%, #660000 100%);
        }"""
content = content.replace(old_root, new_root)

# 2. Change hardcoded RGBA cyan colors (0, 229, 255) to Crimson (255, 0, 60)
content = content.replace("rgba(0, 229, 255,", "rgba(255, 0, 60,")
content = content.replace("rgba(0,229,255,", "rgba(255,0,60,")
content = content.replace("#00e5ff", "#ff003c")
content = content.replace("#0055ff", "#660000")
content = content.replace("#00ffff", "#ff003c")
content = content.replace("#0077ff", "#660000")

# 3. Change Snow to floating Demonic Embers
old_snow_css = """        .snowflake {
            position: absolute; background: #fff; box-shadow: 0 0 5px rgba(255,255,255,0.5);
            animation: fall linear infinite; top: -10px;
        }
        @keyframes fall {
            0% { transform: translateY(-10px) translateX(0); }
            100% { transform: translateY(105vh) translateX(30px); }
        }"""
new_snow_css = """        .snowflake {
            position: absolute; background: #ff4500; box-shadow: 0 0 10px #ff0000; border-radius: 50%;
            animation: fall linear infinite; bottom: -10px;
        }
        @keyframes fall {
            0% { transform: translateY(105vh) translateX(0) scale(1); opacity: 1; }
            100% { transform: translateY(-10px) translateX(40px) scale(0.2); opacity: 0; }
        }"""
content = content.replace(old_snow_css, new_snow_css)

# Update the dark overlay to have a deep red tint
content = content.replace("rgba(5,15,20,0.2) 0%, rgba(0,0,0,0.65)", "rgba(20,0,0,0.3) 0%, rgba(10,0,0,0.85)")

# Change hardcoded colors in specific components
content = content.replace("background: #0a1e23", "background: #0a0000") # Login modal
content = content.replace("background: rgba(10, 30, 35, 0.85)", "background: rgba(15, 0, 0, 0.9)") # Details modal
content = content.replace("border: 1px solid #1a3035;", "border: 1px solid #300000;") # SysReq border

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

