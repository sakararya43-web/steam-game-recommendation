import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Wider video screen
content = content.replace("flex: 1.3; background: #000; position: relative;", "flex: 2; background: #000; position: relative;")

# 2. Add padding to sysreq ul/li
sysreq_css_old = """        .modal-sysreq-content {
            font-family: 'Consolas', monospace; font-size: 0.85rem; color: #a0b6b8; line-height: 1.6;
            background: #050a0f; padding: 12px; border-radius: 8px; border: 1px solid #1a3035;
        }"""
sysreq_css_new = """        .modal-sysreq-content {
            font-family: 'Consolas', monospace; font-size: 0.85rem; color: #a0b6b8; line-height: 1.6;
            background: #050a0f; padding: 12px; border-radius: 8px; border: 1px solid #1a3035;
        }
        .modal-sysreq-content ul { padding-left: 20px; margin: 10px 0; }
        .modal-sysreq-content li { margin-bottom: 8px; }"""
content = content.replace(sysreq_css_old, sysreq_css_new)

# 3. Add "Price: " prefix
price_js_old = """                    if (data.price && data.price.final_formatted) {
                        priceBadge.style.display = "inline-flex";
                        priceBadge.innerText = data.price.discount_percent > 0 
                            ? `${data.price.final_formatted} (-${data.price.discount_percent}%)` 
                            : data.price.final_formatted;
                    }"""
price_js_new = """                    if (data.price && data.price.final_formatted) {
                        priceBadge.style.display = "inline-flex";
                        priceBadge.innerText = data.price.discount_percent > 0 
                            ? `Price: ${data.price.final_formatted} (-${data.price.discount_percent}%)` 
                            : `Price: ${data.price.final_formatted}`;
                    }"""
content = content.replace(price_js_old, price_js_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

