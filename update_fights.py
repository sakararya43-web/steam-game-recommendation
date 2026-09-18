import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the slides with fighting cinematic backgrounds and 5 slides
old_slideshow_html = """    <div class="bg-slideshow">
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
    </div>"""

new_slideshow_html = """    <div class="bg-slideshow">
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
    </div>"""
content = content.replace(old_slideshow_html, new_slideshow_html)

old_slide_css = """        .bg-slide {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover; background-position: center; opacity: 0;
            animation: fadeCycle 40s infinite;
        }
        .bg-slide:nth-child(1) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1091500/page_bg_generated_v6b.jpg'); animation-delay: 0s; }
        .bg-slide:nth-child(2) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/page_bg_generated_v6b.jpg'); animation-delay: 10s; }
        .bg-slide:nth-child(3) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1174180/page_bg_generated_v6b.jpg'); animation-delay: 20s; }
        .bg-slide:nth-child(4) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/page_bg_generated_v6b.jpg'); animation-delay: 30s; }

        @keyframes fadeCycle {
            0%, 20% { opacity: 1; }
            25%, 95% { opacity: 0; }
            100% { opacity: 1; }
        }"""

new_slide_css = """        .bg-slide {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover; background-position: center; opacity: 0;
            animation: fadeCycle 50s infinite;
        }
        .bg-slide:nth-child(1) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/782330/page_bg_generated_v6b.jpg'); animation-delay: 0s; } /* DOOM Eternal */
        .bg-slide:nth-child(2) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/814380/page_bg_generated_v6b.jpg'); animation-delay: 10s; } /* Sekiro */
        .bg-slide:nth-child(3) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/976310/page_bg_generated_v6b.jpg'); animation-delay: 20s; } /* Mortal Kombat 11 */
        .bg-slide:nth-child(4) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1778820/page_bg_generated_v6b.jpg'); animation-delay: 30s; } /* Tekken 8 */
        .bg-slide:nth-child(5) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/582010/page_bg_generated_v6b.jpg'); animation-delay: 40s; } /* Monster Hunter World */

        @keyframes fadeCycle {
            0%, 15% { opacity: 1; }
            20%, 95% { opacity: 0; }
            100% { opacity: 1; }
        }"""
content = content.replace(old_slide_css, new_slide_css)

# Further decrease overlay darkness so the images POP out.
old_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(5,15,20,0.4) 0%, rgba(0,0,0,0.85) 100%);
        }"""
new_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(5,15,20,0.2) 0%, rgba(0,0,0,0.65) 100%);
        }"""
content = content.replace(old_overlay, new_overlay)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

