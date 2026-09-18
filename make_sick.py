import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace modal CSS
old_modal_css = """        .modal {
            background: #0a1e23; border: 1px solid var(--glass-border); border-radius: 20px; width: 90%; max-width: 900px;
            text-align: left; box-shadow: 0 20px 50px rgba(0,0,0,0.8); position: relative; overflow: hidden; animation: slideUp 0.3s;
        }"""
new_modal_css = """        .modal {
            background: rgba(10, 30, 35, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 24px; width: 95%; max-width: 1200px;
            text-align: left; box-shadow: 0 30px 60px rgba(0,0,0,0.9), 0 0 40px rgba(0, 229, 255, 0.1); 
            position: relative; overflow: hidden; animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex; flex-direction: row; max-height: 85vh;
        }
        @media (max-width: 900px) {
            .modal { flex-direction: column; overflow-y: auto; }
            .modal-left { min-height: 300px; }
            .modal-right { overflow-y: visible !important; }
        }
        .modal-left {
            flex: 1.3; background: #000; position: relative; border-right: 1px solid rgba(255,255,255,0.05);
        }
        .modal-right {
            flex: 1; padding: 40px; display: flex; flex-direction: column; overflow-y: auto;
        }
        .modal-right::-webkit-scrollbar { width: 6px; }
        .modal-right::-webkit-scrollbar-thumb { background: rgba(0,229,255,0.3); border-radius: 10px; }
"""
content = content.replace(old_modal_css, new_modal_css)

# Replace modal HTML
old_modal_html = """        <div class="modal">
            <button class="close-modal" onclick="closeDetailsModal()">&times;</button>
            <div class="modal-body">
                <h2 id="modalTitle" style="font-family: 'Poppins'; margin-bottom: 5px; font-size: 1.8rem;"></h2>
                
                <div class="modal-header-info">
                    <span id="modalDevs" style="color: var(--primary); font-weight: 600;"></span>
                    <span id="modalRating" class="modal-rating-badge"></span>
                    <span id="modalPrice" class="modal-rating-badge" style="background: rgba(0, 229, 255, 0.1); border: 1px solid var(--primary); display: none;"></span>
                </div>

                <div id="mediaContainer" style="width: 100%; height: 400px; background: #000; position: relative; border-radius: 12px; overflow: hidden; margin: 25px 0; border: 2px solid rgba(0, 229, 255, 0.4); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);">
                    <img id="modalImg" src="" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top:0; left:0;">
                    <video id="modalVideo" controls autoplay muted style="width: 100%; height: 100%; position: absolute; top:0; left:0; display: none; object-fit: contain; background: #000; z-index: 10;"></video>
                </div>
                
                <div class="modal-section">
                    <h3>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        About This Game
                    </h3>
                    <div id="modalDesc" class="modal-desc-content" style="max-height: 100px; overflow: hidden; position: relative; transition: max-height 0.3s ease;"></div>
                    <button id="modalDescToggle" onclick="toggleDesc()" style="background: none; border: none; color: var(--primary); cursor: pointer; padding: 5px 0; font-family: 'Inter'; display: none;">Read More ▼</button>
                </div>
                
                <div class="modal-section">
                    <h3>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20 18c1.1 0 1.99-.9 1.99-2L22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2H0v2h24v-2h-4zM4 6h16v10H4V6z"/></svg>
                        System Requirements
                    </h3>
                    <div id="modalSysReq" class="modal-sysreq-content"></div>
                </div>
                
                <button id="modalFindBtn" class="btn-action" style="margin-top: 20px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                    Find Similar Games
                </button>
            </div>
        </div>"""

new_modal_html = """        <div class="modal">
            <button class="close-modal" onclick="closeDetailsModal()">&times;</button>
            
            <div class="modal-left">
                <img id="modalImg" src="" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top:0; left:0; filter: brightness(0.8);">
                <video id="modalVideo" controls autoplay muted style="width: 100%; height: 100%; position: absolute; top:0; left:0; display: none; object-fit: cover; background: #000; z-index: 10;"></video>
                <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 150px; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); z-index: 11; pointer-events: none;"></div>
            </div>

            <div class="modal-right">
                <h2 id="modalTitle" style="font-family: 'Poppins'; margin-bottom: 15px; font-size: 2.2rem; background: linear-gradient(to right, #fff, #a0b6b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"></h2>
                
                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 25px;">
                    <span id="modalRating" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);"></span>
                    <span id="modalDevs" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--primary);"></span>
                    <span id="modalPrice" class="modal-rating-badge" style="font-size: 0.9rem; padding: 6px 12px; background: rgba(0, 229, 255, 0.15); border: 1px solid var(--primary); display: none; font-weight: 700; box-shadow: 0 0 10px rgba(0,229,255,0.3);"></span>
                </div>
                
                <div class="modal-section" style="background: rgba(0,0,0,0.3); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                    <h3 style="color: #fff; font-size: 1.1rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="var(--primary)"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        About This Game
                    </h3>
                    <div id="modalDesc" class="modal-desc-content" style="max-height: 120px; overflow: hidden; position: relative; transition: max-height 0.4s ease; font-size: 0.95rem; line-height: 1.6; color: rgba(255,255,255,0.8);"></div>
                    <button id="modalDescToggle" onclick="toggleDesc()" style="background: none; border: none; color: var(--primary); cursor: pointer; padding: 10px 0 0 0; font-family: 'Inter'; font-weight: 600; display: none; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px;">Read More ▼</button>
                </div>
                
                <div class="modal-section" style="margin-top: 20px;">
                    <h3 style="color: rgba(255,255,255,0.6); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20 18c1.1 0 1.99-.9 1.99-2L22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2H0v2h24v-2h-4zM4 6h16v10H4V6z"/></svg>
                        System Requirements
                    </h3>
                    <div id="modalSysReq" class="modal-sysreq-content" style="background: #000; padding: 15px; border-radius: 8px; border-left: 3px solid rgba(255,255,255,0.2);"></div>
                </div>
                
                <div style="flex-grow: 1;"></div>
                
                <button id="modalFindBtn" class="btn-action" style="margin-top: 30px; justify-content: center; box-shadow: 0 10px 20px rgba(0,229,255,0.2); transition: 0.3s; transform: scale(1);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                    Find Similar Games
                </button>
            </div>
        </div>"""

content = content.replace(old_modal_html, new_modal_html)

# Also update the toggleDesc to use 120px
content = content.replace("desc.style.maxHeight === '100px'", "desc.style.maxHeight === '120px'")
content = content.replace("desc.style.maxHeight = '100px'", "desc.style.maxHeight = '120px'")
content = content.replace("scrollHeight > 100", "scrollHeight > 120")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

