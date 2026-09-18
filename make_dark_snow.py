import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body CSS and add new CSS
body_css_old = """        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            background-image: url('assets/bg.png');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }"""
body_css_new = """        body {
            font-family: 'Inter', sans-serif;
            background-color: #000;
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* Cinematic Background Slideshow */
        .bg-slideshow { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -3; }
        .bg-slide {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover; background-position: center; opacity: 0;
            animation: fadeCycle 40s infinite;
        }
        .bg-slide:nth-child(1) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1091500/page_bg_generated_v6b.jpg'); animation-delay: 0s; }
        .bg-slide:nth-child(2) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/page_bg_generated_v6b.jpg'); animation-delay: 10s; }
        .bg-slide:nth-child(3) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1174180/page_bg_generated_v6b.jpg'); animation-delay: 20s; }
        .bg-slide:nth-child(4) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/page_bg_generated_v6b.jpg'); animation-delay: 30s; }

        @keyframes fadeCycle {
            0%, 20% { opacity: 0.5; }
            25%, 95% { opacity: 0; }
            100% { opacity: 0.5; }
        }

        /* Dark Overlay */
        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -2;
            background: radial-gradient(circle at center, rgba(5,15,20,0.85) 0%, rgba(0,0,0,0.98) 100%);
        }

        /* Pixel Snow */
        #snow-container {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; pointer-events: none; overflow: hidden;
        }
        .snowflake {
            position: absolute; background: #fff; box-shadow: 0 0 5px rgba(255,255,255,0.5);
            animation: fall linear infinite; top: -10px;
        }
        @keyframes fall {
            0% { transform: translateY(-10px) translateX(0); }
            100% { transform: translateY(105vh) translateX(30px); }
        }"""
content = content.replace(body_css_old, body_css_new)

# 2. Add the divs after <body>
body_tag = "<body>"
new_body_html = """<body>
    <!-- Cinematic Background -->
    <div class="bg-slideshow">
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
    </div>
    <div class="bg-overlay"></div>
    <div id="snow-container"></div>"""
content = content.replace(body_tag, new_body_html)

# 3. Add JS function to initialize snow
onload_old = "window.onload = () => fetchPopular();"
onload_new = """window.onload = () => {
            fetchPopular();
            createSnow();
        };

        function createSnow() {
            const container = document.getElementById('snow-container');
            for(let i=0; i<150; i++) {
                let flake = document.createElement('div');
                flake.className = 'snowflake';
                // Pixelated snow size
                let size = [2, 3, 4][Math.floor(Math.random() * 3)];
                flake.style.width = size + 'px';
                flake.style.height = size + 'px';
                flake.style.left = Math.random() * 100 + 'vw';
                flake.style.opacity = Math.random() * 0.4 + 0.1;
                flake.style.animationDuration = (Math.random() * 10 + 5) + 's';
                flake.style.animationDelay = (Math.random() * 10) + 's';
                container.appendChild(flake);
            }
        }"""
content = content.replace(onload_old, onload_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

