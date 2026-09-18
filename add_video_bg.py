import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the static slideshow with a video background
old_slideshow = """    <!-- Cinematic Background -->
    <div class="bg-slideshow">
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
        <div class="bg-slide"></div>
    </div>"""

new_slideshow = """    <!-- Moving Cinematic Fights Background -->
    <video id="bgVideo" autoplay muted playsinline style="position:fixed; top:0; left:0; width:100vw; height:100vh; object-fit:cover; z-index:0; filter: brightness(1.5);"></video>"""
content = content.replace(old_slideshow, new_slideshow)

# Remove the old bg-slideshow CSS
css_to_remove = re.compile(r'/\* Cinematic Background Slideshow \*/.*?@keyframes fadeCycle \{.*?\}', re.DOTALL)
content = css_to_remove.sub('', content)

# Reduce the overlay opacity to make the fights pop out
old_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(20,0,0,0.3) 0%, rgba(10,0,0,0.85) 100%);
        }"""
new_overlay = """        .bg-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
            background: radial-gradient(circle at center, rgba(20,0,0,0.1) 0%, rgba(10,0,0,0.65) 100%);
        }"""
content = content.replace(old_overlay, new_overlay)

# Add the JS to play the videos
old_onload = """        window.onload = () => {
            fetchPopular();
            createSnow();
        };"""

new_onload = """        const fightTrailers = [
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
content = content.replace(old_onload, new_onload)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

