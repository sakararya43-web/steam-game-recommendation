import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_snow = """        .snowflake {
            position: absolute; background: #ff4500; box-shadow: 0 0 10px #ff0000; border-radius: 50%;
            animation: fall linear infinite; bottom: -10px;
        }
        @keyframes fall {
            0% { transform: translateY(105vh) translateX(0) scale(1); opacity: 1; }
            100% { transform: translateY(-10px) translateX(40px) scale(0.2); opacity: 0; }
        }"""

new_snow = """        .snowflake {
            position: absolute; background: #ff0000; box-shadow: 0 0 5px rgba(255,0,0,0.8);
            animation: fall linear infinite; top: -10px;
        }
        @keyframes fall {
            0% { transform: translateY(-10px) translateX(0); opacity: 1; }
            100% { transform: translateY(105vh) translateX(30px); opacity: 0.2; }
        }"""
content = content.replace(old_snow, new_snow)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

