import re

with open("C:/Users/BRUNO/Downloads/schedule-buddy-app-65-main/LANDING PAGE TATÁ/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Google Fonts
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

# 2. CSS Variables
content = content.replace(
    "--font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;",
    "--font: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;\n      --font-heading: 'Oswald', -apple-system, BlinkMacSystemFont, sans-serif;"
)
content = content.replace("--max-width: 1100px;", "--max-width: 1400px;")

# 3. Typography & Sizes
content = content.replace("font-size: clamp(1.6rem, 3.5vw, 2.4rem);", "font-size: clamp(2.4rem, 4.5vw, 3.6rem);\n      font-family: var(--font-heading); text-transform: uppercase;")
content = content.replace("font-size: clamp(2rem, 4.5vw, 3rem); font-weight: 900;", "font-size: clamp(3rem, 6vw, 5rem); font-weight: 700; font-family: var(--font-heading); text-transform: uppercase;")
content = content.replace("font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 900;", "font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; font-family: var(--font-heading);")
content = content.replace("padding: 14px 28px; border-radius: var(--radius); font-family: var(--font);\n      font-size: 0.95rem; font-weight: 600;", "padding: 18px 36px; border-radius: var(--radius); font-family: var(--font-heading); text-transform: uppercase; letter-spacing: 0.05em;\n      font-size: 1.15rem; font-weight: 600;")
content = content.replace("font-family: var(--font); font-size: 0.85rem; font-weight: 600;", "font-family: var(--font-heading); text-transform: uppercase; letter-spacing: 0.05em; font-size: 1rem; font-weight: 600;")
content = content.replace("font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 800;", "font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; font-family: var(--font-heading); text-transform: uppercase;")
content = content.replace("font-size: clamp(1.8rem, 4vw, 2.6rem); font-weight: 900;", "font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 700; font-family: var(--font-heading); text-transform: uppercase;")
content = content.replace("font-size: clamp(0.95rem, 1.8vw, 1.05rem);", "font-size: clamp(1.1rem, 2vw, 1.2rem);")
content = content.replace("font-size: clamp(0.95rem, 1.6vw, 1.05rem);", "font-size: clamp(1.1rem, 1.8vw, 1.25rem);")

# 4. Logo size
content = content.replace(".navbar-logo img { height: 36px; width: auto; }", ".navbar-logo img { height: 72px; width: auto; }")

# 5. Table and Hover Animation Improvements
content = content.replace(".mod-card:hover { border-color: var(--orange); transform: translateY(-3px); box-shadow: var(--shadow-glow); }", ".mod-card:hover { border-color: var(--orange); transform: translateY(-8px) scale(1.02); box-shadow: 0 10px 40px rgba(255,106,0,0.2); }")
content = content.replace(".ben-card:hover { border-color: var(--orange); transform: translateY(-2px); box-shadow: var(--shadow-glow); }", ".ben-card:hover { border-color: var(--orange); transform: translateY(-8px) scale(1.02); box-shadow: 0 10px 40px rgba(255,106,0,0.2); }")
content = content.replace(".auth-card:hover { border-color: rgba(255,106,0,0.3); transform: translateY(-2px); }", ".auth-card:hover { border-color: rgba(255,106,0,0.5); transform: translateY(-8px) scale(1.05); box-shadow: 0 10px 40px rgba(255,106,0,0.15); }")
content = content.replace(".plan-m-card:hover { border-color: rgba(255,106,0,0.3); }", ".plan-m-card:hover { border-color: var(--orange); transform: translateY(-4px) scale(1.02); box-shadow: 0 8px 30px rgba(255,106,0,0.2); }")
content = content.replace(".plan-table tbody tr:hover { background: var(--bg-card-hover); }", ".plan-table tbody tr:hover { background: var(--bg-card-hover); transform: scale(1.01); box-shadow: 0 4px 20px rgba(0,0,0,0.3); position: relative; z-index: 10; border-radius: var(--radius-sm); }")
content = content.replace(".plan-table tbody td { padding: 14px 16px; font-size: 0.9rem; vertical-align: middle; }", ".plan-table tbody td { padding: 18px 24px; font-size: 1.05rem; vertical-align: middle; }")
content = content.replace(".plan-table tbody td:last-child { text-align: right; font-weight: 800; color: var(--orange); font-size: 1.05rem;", ".plan-table tbody td:last-child { text-align: right; font-weight: 800; color: var(--orange); font-size: 1.25rem;")

# 6. Text Replacements (musc -> Musculação, aero -> Aeróbica, etc)
# Be careful to only replace within the table areas or text context.
replacements = [
    ("musc +", "Musculação +"),
    (" musc ", " Musculação "),
    (" aero<", " Aeróbica<"),
    (" aero</", " Aeróbica</"),
    (" aeróbica", " Aeróbica"),
    (" musculação", " Musculação"),
    ("+ 1 MT", "+ 1 Muay Thai"),
    ("+ 2 MT", "+ 2 Muay Thai"),
    ("+ 3 MT", "+ 3 Muay Thai"),
    ("+ 1 JJ", "+ 1 Jiu-Jitsu"),
    ("+ 2 JJ", "+ 2 Jiu-Jitsu"),
    ("+ 3 JJ", "+ 3 Jiu-Jitsu")
]
for old, new in replacements:
    content = content.replace(old, new)
    
# Write back
with open("C:/Users/BRUNO/Downloads/schedule-buddy-app-65-main/LANDING PAGE TATÁ/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Update complete")
