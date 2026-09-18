import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make Modal Bigger
content = content.replace("max-width: 650px;", "max-width: 900px;")
content = content.replace("height: 250px;", "height: 450px;") # mediaContainer and modalImg inline styles

# 2. Auto-open modal on search
fetch_rec_old = """                } else {
                    if (data.target) {
                        renderTarget(data.target);
                    }"""
fetch_rec_new = """                } else {
                    if (data.target) {
                        renderTarget(data.target);
                        // Auto-open the big window for the searched game
                        openGameDetails(data.target.name, data.target.appId);
                    }"""
content = content.replace(fetch_rec_old, fetch_rec_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

