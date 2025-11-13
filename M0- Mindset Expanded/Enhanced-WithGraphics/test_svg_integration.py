from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io
from svg_graphics_library import SVG_LIBRARY

# Create a test slide with SVG graphic
WIDTH = 1920
HEIGHT = 1080
BG_LIGHT = (245, 245, 245)
TEXT_DARK = (26, 31, 46)
ACCENT_GOLD = (212, 175, 55)

# Create slide
img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
draw = ImageDraw.Draw(img)

# Add title
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
except:
    font_title = font_body = ImageFont.load_default()

margin = 120
draw.text((margin, margin), "Success Habit #1: Have A Specific Vision", fill=TEXT_DARK, font=font_title)

# Convert SVG to PNG and overlay on slide
svg_code = SVG_LIBRARY['target'](size=150)
png_data = cairosvg.svg2png(bytestring=svg_code.encode('utf-8'))
svg_img = Image.open(io.BytesIO(png_data))

# Position icon in top right
icon_x = WIDTH - margin - 150
icon_y = margin
img.paste(svg_img, (icon_x, icon_y), svg_img if svg_img.mode == 'RGBA' else None)

# Add bullet points
bullets = [
    "Most people don't have a specific vision",
    "What do you want? When? Why?",
    "Clarity of vision helps you keep going when things get hard",
    "Vision is about what you're EXCLUDING",
]

y_offset = margin + 200
for bullet in bullets:
    draw.ellipse([margin, y_offset + 10, margin + 12, y_offset + 22], fill=ACCENT_GOLD)
    draw.text((margin + 30, y_offset), bullet, fill=TEXT_DARK, font=font_body)
    y_offset += 70

# Save
img.save('test-slide-with-svg.png')
print("✓ Created test slide with SVG graphic")
print("  File: test-slide-with-svg.png")
