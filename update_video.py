import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html = """            <div id="mediaContainer" style="width: 100%; height: 450px; background: #000; position: relative; border-radius: 12px 12px 0 0; overflow: hidden;">
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

new_html = """            <div class="modal-body">
                <h2 id="modalTitle" style="font-family: 'Poppins'; margin-bottom: 5px; font-size: 1.8rem;"></h2>
                
                <div class="modal-header-info">
                    <span id="modalDevs" style="color: var(--primary); font-weight: 600;"></span>
                    <span id="modalRating" class="modal-rating-badge"></span>
                    <span id="modalPrice" class="modal-rating-badge" style="background: rgba(0, 229, 255, 0.1); border: 1px solid var(--primary); display: none;"></span>
                </div>

                <div id="mediaContainer" style="width: 100%; height: 400px; background: #000; position: relative; border-radius: 12px; overflow: hidden; margin: 25px 0; border: 2px solid rgba(0, 229, 255, 0.4); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);">
                    <img id="modalImg" src="" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top:0; left:0;">
                    <video id="modalVideo" controls autoplay muted style="width: 100%; height: 100%; position: absolute; top:0; left:0; display: none; object-fit: contain; background: #000; z-index: 10;"></video>
                </div>"""

content = content.replace(old_html, new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

