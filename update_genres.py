import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add span to HTML
old_html = """                    <span id="modalRating" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);"></span>
                    <span id="modalDevs" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--primary);"></span>"""

new_html = """                    <span id="modalRating" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);"></span>
                    <span id="modalDevs" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--primary);"></span>
                    <span id="modalGenres" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: #a0b6b8; display: none;"></span>"""

content = content.replace(old_html, new_html)

# 2. Reset span in JS
old_reset = """            document.getElementById('modalRating').innerText = "Loading Rating...";
            document.getElementById('modalDevs').innerText = "";"""
new_reset = """            document.getElementById('modalRating').innerText = "Loading Rating...";
            document.getElementById('modalDevs').innerText = "";
            document.getElementById('modalGenres').style.display = "none";
            document.getElementById('modalGenres').innerText = "";"""
content = content.replace(old_reset, new_reset)

# 3. Populate span in JS
old_pop = """                    document.getElementById('modalSysReq').innerHTML = data.sysReq;
                    document.getElementById('modalRating').innerText = data.rating;
                    document.getElementById('modalDevs').innerText = data.devs;"""
new_pop = """                    document.getElementById('modalSysReq').innerHTML = data.sysReq;
                    document.getElementById('modalRating').innerText = data.rating;
                    document.getElementById('modalDevs').innerText = data.devs;
                    
                    if (data.genres) {
                        document.getElementById('modalGenres').style.display = "inline-flex";
                        document.getElementById('modalGenres').innerText = data.genres;
                    }"""
content = content.replace(old_pop, new_pop)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

