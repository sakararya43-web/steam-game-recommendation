import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add JS function
script_start = """    <script>
        const API_BASE = "https://steam-game-recommendation-2.onrender.com";"""

new_script_start = """    <script>
        const API_BASE = "https://steam-game-recommendation-2.onrender.com";

        function handleImageError(img, appId) {
            if (!img.dataset.retry) {
                img.dataset.retry = "1";
                img.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/capsule_616x353.jpg`;
            } else if (img.dataset.retry === "1") {
                img.dataset.retry = "2";
                img.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/library_600x900.jpg`;
            } else if (img.dataset.retry === "2") {
                img.dataset.retry = "3";
                img.src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/logo.png`;
            } else {
                img.onerror = null;
                img.src = 'https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image';
            }
        }"""
content = content.replace(script_start, new_script_start)

# Replace target image
old_target = """<img src="${imgUrl}" style="width: 250px; height: 100%; object-fit: cover;" onerror="this.onerror=null; this.src='https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image'">"""
new_target = """<img src="${imgUrl}" style="width: 250px; height: 100%; object-fit: cover;" onerror="handleImageError(this, '${target.appId}')">"""
content = content.replace(old_target, new_target)

# Replace grid image
old_grid = """<img src="${imgUrl}" alt="${item.name}" onerror="this.onerror=null; this.src='https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image'">"""
new_grid = """<img src="${imgUrl}" alt="${item.name}" onerror="handleImageError(this, '${item.appId}')">"""
content = content.replace(old_grid, new_grid)

# Replace modal image
old_modal = """            imgEl.onerror = function() { this.onerror=null; this.src='https://placehold.co/600x400/0a1e23/00e5ff?text=No+Image'; };"""
new_modal = """            imgEl.onerror = function() { handleImageError(this, appId); };"""
content = content.replace(old_modal, new_modal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

