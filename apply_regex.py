import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace modal HTML using regex to avoid exact string mismatches
pattern = re.compile(r'<div class="modal">.*?</div>\s*</div>\s*</div>\s*<script>', re.DOTALL)

new_modal_html = """<div class="modal">
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
                
                <button class="btn-action" id="modalFindBtn" style="margin-top: 30px; justify-content: center; box-shadow: 0 10px 20px rgba(0,229,255,0.2); transition: 0.3s; transform: scale(1);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
                    Find Similar Games
                </button>
            </div>
        </div>
    </div>

    <script>"""

content = pattern.sub(new_modal_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

