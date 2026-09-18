import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace video tag with slideshow divs
old_video = """    <!-- Moving Cinematic Fights Background -->
    <video id="bgVideo" autoplay muted playsinline style="position:fixed; top:0; left:0; width:100vw; height:100vh; object-fit:cover; z-index:0; filter: brightness(1.5);"></video>"""
new_slideshow = """    <!-- Cinematic Background -->
    <div class="bg-slideshow">
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
    </div>"""
content = content.replace(old_video, new_slideshow)

# 2. Inject the Slideshow CSS into the <style> section
# I'll inject it right after `flex-direction: column; }` in body
body_end = """        body {
            font-family: 'Inter', sans-serif;
            background-color: #000;
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }"""
slideshow_css = """

        /* Cinematic Background Slideshow */
        .bg-slideshow { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; }
        .bg-slide {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover; background-position: center; opacity: 0;
            animation: fadeCycle 50s infinite;
        }
        .bg-slide:nth-child(1) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/782330/page_bg_generated_v6b.jpg'); animation-delay: 0s; }
        .bg-slide:nth-child(2) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/814380/page_bg_generated_v6b.jpg'); animation-delay: 10s; }
        .bg-slide:nth-child(3) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/976310/page_bg_generated_v6b.jpg'); animation-delay: 20s; }
        .bg-slide:nth-child(4) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1778820/page_bg_generated_v6b.jpg'); animation-delay: 30s; }
        .bg-slide:nth-child(5) { background-image: url('https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/582010/page_bg_generated_v6b.jpg'); animation-delay: 40s; }

        @keyframes fadeCycle {
            0%, 15% { opacity: 1; }
            20%, 95% { opacity: 0; }
            100% { opacity: 1; }
        }"""
content = content.replace(body_end, body_end + slideshow_css)

# 3. Remove the video JS
video_js = """        const fightTrailers = [
            "https://video.akamai.steamstatic.com/store_trailers/782330/1058653592/9f0464e095deedf33609b7717ae0390d6fa20ffb/1755007462/hls_264_master.m3u8?t=1755109909",
            "https://video.akamai.steamstatic.com/store_trailers/814380/322401/63cf1fdf9c16536f04b08a5b1939909f7a99a340/1750586450/hls_264_master.m3u8?t=1603837979",
            "https://video.akamai.steamstatic.com/store_trailers/976310/332672/8f6e1b6366ce432e28d6e3df6d5b97e09a0a0a44/1750603056/hls_264_master.m3u8?t=1607567246",
            "https://video.akamai.steamstatic.com/store_trailers/1778820/607697/cdc675753758d3c36c0937463bdfd01f4b227825/1750735029/hls_264_master.m3u8?t=1695192962"
        ];
        let currentTrailer = 0;
        let bgHls = null;

        function playBgVideo() {
            const video = document.getElementById('bgVideo');
            if (Hls.isSupported()) {
                if (bgHls) bgHls.destroy();
                bgHls = new Hls();
                bgHls.loadSource(fightTrailers[currentTrailer]);
                bgHls.attachMedia(video);
                bgHls.on(Hls.Events.MANIFEST_PARSED, function() {
                    video.play();
                });
                video.onended = () => {
                    currentTrailer = (currentTrailer + 1) % fightTrailers.length;
                    playBgVideo();
                };
            }
        }

        window.onload = () => {
            fetchPopular();
            createSnow();
            playBgVideo();
        };"""
new_onload = """        window.onload = () => {
            fetchPopular();
            createSnow();
        };"""
content = content.replace(video_js, new_onload)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

