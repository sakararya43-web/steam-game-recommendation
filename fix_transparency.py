import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the card hover overlay transparent black instead of opaque grey
old_card_before = """        .card::before {
            content: 'View Details'; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(200, 200, 200, 0.85); color: #000; font-weight: 800; font-family: 'Poppins', sans-serif;
            font-size: 1.2rem; display: flex; justify-content: center; align-items: center; opacity: 0; transition: opacity 0.3s; z-index: 10;
        }"""

new_card_before = """        .card::before {
            content: 'View Details'; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.5); color: #fff; font-weight: 800; font-family: 'Poppins', sans-serif;
            font-size: 1.2rem; display: flex; justify-content: center; align-items: center; opacity: 0; transition: opacity 0.3s; z-index: 10;
        }"""

content = content.replace(old_card_before, new_card_before)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

