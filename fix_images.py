import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the sits_01.png fallbacks
old_onerror = """onerror="this.src='https://community.cloudflare.steamstatic.com/public/images/signinthroughsteam/sits_01.png'\""""
new_onerror = """onerror="this.onerror=null; this.src='https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image'\""""
content = content.replace(old_onerror, new_onerror)

# Add onerror to modalImg in JS
old_modal_img = """            document.getElementById('modalImg').src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            document.getElementById('modalImg').style.display = "block";"""
new_modal_img = """            const imgEl = document.getElementById('modalImg');
            imgEl.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            imgEl.onerror = function() { this.onerror=null; this.src='https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image'; };
            imgEl.style.display = "block";"""
content = content.replace(old_modal_img, new_modal_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

