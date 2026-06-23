import re

with open("C:/Users/BRUNO/Downloads/schedule-buddy-app-65-main/LANDING PAGE TATÁ/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the grid CSS
old_grid_css = ".loc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }"
new_grid_css = """.loc-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; align-items: stretch; }
    .loc-figure { width: 100%; border-radius: var(--radius-lg); overflow: hidden; display: flex; align-items: center; justify-content: center; background: var(--bg-card); border: 1px solid var(--gray-border); }
    .loc-figure img { width: 100%; height: 100%; object-fit: cover; object-position: top; }"""
content = content.replace(old_grid_css, new_grid_css)

old_mobile_css = "@media(max-width:768px) { .loc-grid { grid-template-columns: 1fr; } .loc-map { min-height: 280px; } }"
new_mobile_css = "@media(max-width:900px) { .loc-grid { grid-template-columns: 1fr; } .loc-map, .loc-figure { min-height: 350px; } }"
content = content.replace(old_mobile_css, new_mobile_css)

# 2. Update the HTML section
old_html = """        <div class="loc-map anim-right">
          <!-- Insert Google Maps iframe here: <iframe src="YOUR_MAPS_EMBED_URL" allowfullscreen loading="lazy"></iframe> -->
        </div>
      </div>"""

new_html = """        <div class="loc-map anim-right">
          <iframe src="https://www.google.com/maps?q=Av.+Montes+Claros,+81+Rio+Pardo+de+Minas&output=embed" allowfullscreen loading="lazy"></iframe>
        </div>
        <div class="loc-figure anim-right" style="transition-delay: .2s">
          <img src="action-figure.png" alt="Action Figure Sports Tatá Fight" loading="lazy">
        </div>
      </div>"""

content = content.replace(old_html, new_html)

# Also ensure map height is set correctly
content = content.replace(".loc-map iframe { width: 100%; height: 100%; min-height: 360px; border: 0; }", ".loc-map iframe { width: 100%; height: 100%; min-height: 100%; border: 0; display: block; }")
content = content.replace(".loc-map { width: 100%; min-height: 360px; background: var(--bg-card); border-radius: var(--radius-lg); border: 1px solid var(--gray-border); overflow: hidden; }", ".loc-map { width: 100%; min-height: 360px; background: var(--bg-card); border-radius: var(--radius-lg); border: 1px solid var(--gray-border); overflow: hidden; display: flex; flex-direction: column; }")


with open("C:/Users/BRUNO/Downloads/schedule-buddy-app-65-main/LANDING PAGE TATÁ/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Location section updated")
