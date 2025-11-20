#!/usr/bin/env python3
"""
Generate updated Slide 11 with new terminology
"""

from PIL import Image, ImageDraw, ImageFont

# Canvas settings
WIDTH = 1920
HEIGHT = 1080
BACKGROUND_COLOR = (245, 245, 245)
TEXT_COLOR = (0, 0, 0)

def get_font(size):
    """Get Helvetica font or fallback"""
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        try:
            return ImageFont.truetype("Helvetica", size)
        except:
            return ImageFont.load_default()

def create_slide_11():
    """Create updated Slide 11 with new terminology"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = get_font(50)
    body_font = get_font(28)
    table_font = get_font(24)
    small_font = get_font(22)

    # Title
    draw.text((30, 30), "Understanding the Landscape", fill=TEXT_COLOR, font=title_font)

    # Left column - role list
    y = 120
    roles = [
        "• Global Account Director - (Enterprise Leaders)",
        "• Global Account Director (Growth Champions)",
        "• Enterprise AE - (Enterprise Leaders)",
        "• Enterprise AE - (Growth Champions)",
        "• Enterprise AE - (Venture-Backed Startups)",
        "• Mid-market AE - (Enterprise Leaders)",
        "• Mid-market AE (Growth Champions)",
        "• Small Business AE (Enterprise Leaders)",
        "• Small Business AE (Growth Champions)",
        "• Small Business AE (Venture-Backed Startups)"
    ]

    for role in roles:
        draw.text((30, y), role, fill=TEXT_COLOR, font=body_font)
        y += 45

    # Right column - table
    table_x = 1000
    table_y = 150
    col_width = 280
    row_height = 120

    # Table headers
    headers = ["Company\nProfile", "Company\nType", "Example"]
    for i, header in enumerate(headers):
        x = table_x + (i * col_width)
        # Draw header background
        draw.rectangle([x, table_y, x + col_width - 10, table_y + row_height - 10], outline=TEXT_COLOR, width=2)
        # Draw header text (centered)
        lines = header.split('\n')
        text_y = table_y + 20
        for line in lines:
            bbox = table_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            text_x = x + (col_width - text_width) // 2 - 5
            draw.text((text_x, text_y), line, fill=TEXT_COLOR, font=table_font)
            text_y += 35

    # Table rows
    rows = [
        {
            "profile": "Enterprise\nLeaders",
            "type": "Industry Leader/\nHigh-Growth",
            "example": "Salesforce,\nGoogle, AWS"
        },
        {
            "profile": "Growth\nChampions",
            "type": "Rising Star/\nProduct-Led\nSaaS Company",
            "example": "Zoom, Slack,\nMiro, Airtable,\nDociusign"
        },
        {
            "profile": "Venture-\nBacked\nStartups",
            "type": "High-Growth/\nStartups",
            "example": "Ramp, Gong,\nBrex, Rippling,\nDell"
        }
    ]

    current_y = table_y + row_height
    for row_data in rows:
        # Draw cells
        for i, (key, value) in enumerate(row_data.items()):
            x = table_x + (i * col_width)
            # Draw cell border
            draw.rectangle([x, current_y, x + col_width - 10, current_y + row_height - 10], outline=TEXT_COLOR, width=2)
            # Draw cell text
            lines = value.split('\n')
            text_y = current_y + 15
            for line in lines:
                bbox = small_font.getbbox(line)
                text_width = bbox[2] - bbox[0]
                text_x = x + (col_width - text_width) // 2 - 5
                draw.text((text_x, text_y), line, fill=TEXT_COLOR, font=small_font)
                text_y += 28

        current_y += row_height

    return img

def main():
    print("Generating updated Slide 11...")
    slide = create_slide_11()
    output_path = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/11.png"
    slide.save(output_path)
    print(f"✓ Saved {output_path}")

if __name__ == "__main__":
    main()
