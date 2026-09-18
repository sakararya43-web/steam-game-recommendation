import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure target img has alt
old_target = """<img src="${imgUrl}" style="width: 250px; height: 100%; object-fit: cover;" onerror="handleImageError(this, '${target.appId}')">"""
new_target = """<img src="${imgUrl}" alt="${target.name}" style="width: 250px; height: 100%; object-fit: cover;" onerror="handleImageError(this, '${target.appId}')">"""
content = content.replace(old_target, new_target)

# Make sure modal img has alt
old_modal = """            const imgEl = document.getElementById('modalImg');
            imgEl.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            imgEl.onerror = function() { handleImageError(this, appId); };"""
new_modal = """            const imgEl = document.getElementById('modalImg');
            imgEl.alt = name;
            imgEl.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            imgEl.onerror = function() { handleImageError(this, appId); };"""
content = content.replace(old_modal, new_modal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

