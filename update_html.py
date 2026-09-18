import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Modal HTML
modal_old = """            <button class="close-modal" onclick="closeDetailsModal()">&times;</button>
            <img id="modalImg" src="" style="width: 100%; height: 250px; object-fit: cover;">
            <div class="modal-body">
                <h2 id="modalTitle" style="font-family: 'Poppins'; margin-bottom: 5px; font-size: 1.8rem;"></h2>
                
                <div class="modal-header-info">
                    <span id="modalDevs" style="color: var(--primary); font-weight: 600;"></span>
                    <span id="modalRating" class="modal-rating-badge"></span>
                </div>"""

modal_new = """            <button class="close-modal" onclick="closeDetailsModal()">&times;</button>
            <div id="mediaContainer" style="width: 100%; height: 250px; background: #000; position: relative; border-radius: 12px 12px 0 0; overflow: hidden;">
                <img id="modalImg" src="" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top:0; left:0;">
                <video id="modalVideo" controls autoplay muted style="width: 100%; height: 100%; position: absolute; top:0; left:0; display: none; object-fit: contain; background: #000; z-index: 10;"></video>
            </div>
            <div class="modal-body">
                <h2 id="modalTitle" style="font-family: 'Poppins'; margin-bottom: 5px; font-size: 1.8rem;"></h2>
                
                <div class="modal-header-info">
                    <span id="modalDevs" style="color: var(--primary); font-weight: 600;"></span>
                    <span id="modalRating" class="modal-rating-badge"></span>
                    <span id="modalPrice" class="modal-rating-badge" style="background: rgba(0, 229, 255, 0.1); border: 1px solid var(--primary); display: none;"></span>
                </div>"""

content = content.replace(modal_old, modal_new)

# 2. Add an Expand/Collapse description toggle
desc_old = """                    <div id="modalDesc" class="modal-desc-content"></div>"""
desc_new = """                    <div id="modalDesc" class="modal-desc-content" style="max-height: 100px; overflow: hidden; position: relative; transition: max-height 0.3s ease;"></div>
                    <button id="modalDescToggle" onclick="toggleDesc()" style="background: none; border: none; color: var(--primary); cursor: pointer; padding: 5px 0; font-family: 'Inter'; display: none;">Read More ▼</button>"""
content = content.replace(desc_old, desc_new)

# 3. Add toggleDesc function and global hls variable
script_start = """    <script>
        const API_BASE = "https://steam-game-recommendation-2.onrender.com";
        let currentSteamId = "";"""

script_new = """    <script>
        const API_BASE = "https://steam-game-recommendation-2.onrender.com";
        let currentSteamId = "";
        let hlsPlayer = null;

        function toggleDesc() {
            const desc = document.getElementById('modalDesc');
            const btn = document.getElementById('modalDescToggle');
            if (desc.style.maxHeight === '100px') {
                desc.style.maxHeight = '1000px';
                btn.innerText = 'Read Less ▲';
            } else {
                desc.style.maxHeight = '100px';
                btn.innerText = 'Read More ▼';
            }
        }"""
content = content.replace(script_start, script_new)

# 4. Handle fetchRecommendations target game
fetch_rec_old = """                if (data.error) {
                    grid.innerHTML = `<p style="color:#00e5ff; font-size: 1.2rem; grid-column: 1/-1;">Game not found. Try another search.</p>`;
                } else if (data.recommendations) {
                    renderGrid(data.recommendations, true);
                }"""
fetch_rec_new = """                if (data.error) {
                    grid.innerHTML = `<p style="color:#00e5ff; font-size: 1.2rem; grid-column: 1/-1;">${data.error}</p>`;
                } else {
                    if (data.target) {
                        renderTarget(data.target);
                    }
                    if (data.recommendations) {
                        renderGrid(data.recommendations, true, !!data.target);
                    }
                }"""
content = content.replace(fetch_rec_old, fetch_rec_new)

# 5. Add renderTarget function before renderGrid
render_target = """        function renderTarget(target) {
            const grid = document.getElementById('mainGrid');
            const imgUrl = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${target.appId}/header.jpg`;
            const heroHtml = `
                <div style="grid-column: 1 / -1; display: flex; background: var(--surface); border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 12px; overflow: hidden; margin-bottom: 20px; align-items: center; cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='rgba(0, 229, 255, 0.2)'" onclick="openGameDetails('${target.name.replace(/'/g, "\\'")}', '${target.appId}')">
                    <img src="${imgUrl}" style="width: 250px; height: 100%; object-fit: cover;" onerror="this.src='https://community.cloudflare.steamstatic.com/public/images/signinthroughsteam/sits_01.png'">
                    <div style="padding: 20px;">
                        <span style="color: var(--primary); font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Searched Game</span>
                        <h2 style="font-family: 'Poppins'; font-size: 1.8rem; margin: 5px 0;">${target.name}</h2>
                        <p style="color: rgba(255,255,255,0.7); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">${target.desc}</p>
                    </div>
                </div>
            `;
            grid.innerHTML = heroHtml;
        }

        function renderGrid"""
content = content.replace("        function renderGrid", render_target)

# 6. Change renderGrid to append instead of clearing if it's recommendations
render_grid_old = """        function renderGrid(items, showMatch) {
            const grid = document.getElementById('mainGrid');
            grid.innerHTML = "";"""
render_grid_new = """        function renderGrid(items, showMatch, append = false) {
            const grid = document.getElementById('mainGrid');
            if (!append) grid.innerHTML = "";"""
content = content.replace(render_grid_old, render_grid_new)

# 7. Update openGameDetails
open_game_old = """        async function openGameDetails(name, appId) {
            const modal = document.getElementById('detailsModal');
            document.getElementById('modalTitle').innerText = name;
            document.getElementById('modalImg').src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            
            document.getElementById('modalDesc').innerHTML = "Loading description from Steam...";
            document.getElementById('modalSysReq').innerHTML = "Loading...";
            document.getElementById('modalRating').innerText = "Loading Rating...";
            document.getElementById('modalDevs').innerText = "";
            
            modal.style.display = 'flex';
            
            document.getElementById('modalFindBtn').onclick = () => {
                closeDetailsModal();
                fetchRecommendations(name, appId);
            };

            try {
                const res = await fetch(API_BASE + `/api/game_details?appId=${appId}`);
                const data = await res.json();
                if (!data.error) {
                    document.getElementById('modalDesc').innerHTML = data.desc;
                    document.getElementById('modalSysReq').innerHTML = data.sysReq;
                    document.getElementById('modalRating').innerText = data.rating;
                    document.getElementById('modalDevs').innerText = data.devs;
                }
            } catch (err) {}
        }"""
open_game_new = """        async function openGameDetails(name, appId) {
            const modal = document.getElementById('detailsModal');
            document.getElementById('modalTitle').innerText = name;
            document.getElementById('modalImg').src = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${appId}/header.jpg`;
            document.getElementById('modalImg').style.display = "block";
            
            const video = document.getElementById('modalVideo');
            video.style.display = "none";
            if (hlsPlayer) { hlsPlayer.destroy(); hlsPlayer = null; }
            video.pause();
            video.removeAttribute('src');
            
            document.getElementById('modalDesc').innerHTML = "Loading description from Steam...";
            document.getElementById('modalDesc').style.maxHeight = '100px';
            document.getElementById('modalDescToggle').style.display = 'none';
            document.getElementById('modalDescToggle').innerText = 'Read More ▼';
            document.getElementById('modalSysReq').innerHTML = "Loading...";
            document.getElementById('modalRating').innerText = "Loading Rating...";
            document.getElementById('modalDevs').innerText = "";
            
            const priceBadge = document.getElementById('modalPrice');
            priceBadge.style.display = "none";
            priceBadge.innerText = "";
            
            modal.style.display = 'flex';
            
            document.getElementById('modalFindBtn').onclick = () => {
                closeDetailsModal();
                fetchRecommendations(name, appId);
            };

            try {
                const res = await fetch(API_BASE + `/api/game_details?appId=${appId}`);
                const data = await res.json();
                if (!data.error) {
                    document.getElementById('modalDesc').innerHTML = data.desc;
                    if (document.getElementById('modalDesc').scrollHeight > 100) {
                        document.getElementById('modalDescToggle').style.display = 'block';
                    }
                    
                    document.getElementById('modalSysReq').innerHTML = data.sysReq;
                    document.getElementById('modalRating').innerText = data.rating;
                    document.getElementById('modalDevs').innerText = data.devs;
                    
                    if (data.price && data.price.final_formatted) {
                        priceBadge.style.display = "inline-flex";
                        priceBadge.innerText = data.price.discount_percent > 0 
                            ? `${data.price.final_formatted} (-${data.price.discount_percent}%)` 
                            : data.price.final_formatted;
                    }
                    
                    if (data.movie) {
                        document.getElementById('modalImg').style.display = "none";
                        video.style.display = "block";
                        if (Hls.isSupported() && data.movie.includes('m3u8')) {
                            hlsPlayer = new Hls();
                            hlsPlayer.loadSource(data.movie);
                            hlsPlayer.attachMedia(video);
                        } else {
                            video.src = data.movie;
                        }
                    }
                }
            } catch (err) {}
        }
        
        function closeDetailsModal() { 
            document.getElementById('detailsModal').style.display = 'none'; 
            if (hlsPlayer) { hlsPlayer.destroy(); hlsPlayer = null; }
            document.getElementById('modalVideo').pause();
        }"""
content = content.replace(open_game_old, open_game_new)

# Also need to remove the duplicate closeDetailsModal from the top
content = content.replace("function closeDetailsModal() { document.getElementById('detailsModal').style.display = 'none'; }", "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

