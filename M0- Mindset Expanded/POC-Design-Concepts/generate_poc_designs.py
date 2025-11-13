from PIL import Image, ImageDraw, ImageFont
import os

# Image dimensions
WIDTH = 1920
HEIGHT = 1080

def create_slide(bg_color, text_color, accent_color, title_text, body_content, concept_name, slide_num, style="default"):
    """
    Create a slide with specific design concept styling

    Args:
        bg_color: Background color tuple (R, G, B)
        text_color: Main text color tuple
        accent_color: Accent color for highlights
        title_text: Main title text
        body_content: List of bullet points or content items
        concept_name: Name of the design concept
        slide_num: Original slide number
        style: Layout style (title, compare, framework, timeline)
    """
    img = Image.new('RGB', (WIDTH, HEIGHT), bg_color)
    draw = ImageDraw.Draw(img)

    # Try to load fonts, fallback to default if not available
    try:
        if concept_name == "Editorial":
            title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf", 72)
        else:
            title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
        body_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
        body_font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 36)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        body_font_bold = ImageFont.load_default()

    margin = 120

    if style == "title":
        # Full-color title slide
        # Title centered vertically and horizontally
        title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]

        title_x = (WIDTH - title_width) // 2
        title_y = (HEIGHT - title_height) // 2

        draw.text((title_x, title_y), title_text, fill=text_color, font=title_font)

        # Add concept-specific accent
        if concept_name == "Executive":
            # Thin line accent above title
            draw.rectangle([title_x, title_y - 40, title_x + 200, title_y - 35], fill=accent_color)
        elif concept_name == "Bold":
            # Bold geometric shape
            draw.ellipse([WIDTH - 300, 100, WIDTH - 100, 300], fill=accent_color)
        elif concept_name == "Editorial":
            # Elegant corner element
            draw.rectangle([margin, margin, margin + 4, margin + 150], fill=accent_color)
            draw.rectangle([margin, margin, margin + 150, margin + 4], fill=accent_color)

    elif style == "compare":
        # Split-screen comparison layout
        # Draw title at top
        draw.text((margin, margin), title_text, fill=text_color, font=title_font)

        # Vertical divider line in center
        center_x = WIDTH // 2
        draw.line([center_x, margin + 150, center_x, HEIGHT - margin], fill=accent_color, width=3)

        # Left side (OLD)
        left_x = margin
        left_y = margin + 180
        draw.text((left_x, left_y), "OLD BELIEFS:", fill=accent_color, font=body_font_bold)

        y_offset = left_y + 60
        for item in body_content[:3]:
            draw.text((left_x, y_offset), item, fill=text_color, font=body_font)
            y_offset += 80

        # Right side (NEW)
        right_x = center_x + 60
        right_y = margin + 180
        draw.text((right_x, right_y), "NEW BELIEFS:", fill=accent_color, font=body_font_bold)

        y_offset = right_y + 60
        for item in body_content[3:]:
            draw.text((right_x, y_offset), item, fill=text_color, font=body_font)
            y_offset += 80

    elif style == "framework":
        # Framework with pillars/boxes
        draw.text((margin, margin), title_text, fill=text_color, font=title_font)

        # Three pillars layout
        start_y = margin + 200
        box_width = 450
        box_height = 500
        spacing = 60

        total_width = (box_width * 3) + (spacing * 2)
        start_x = (WIDTH - total_width) // 2

        pillar_labels = ["Competence", "Preparation", "Evidence"]
        pillar_content = [
            ["Skills create value", "Expertise in areas", "Continuous learning"],
            ["Research companies", "Practice responses", "Mock interviews"],
            ["Document wins", "Quantify results", "Save feedback"]
        ]

        for i in range(3):
            box_x = start_x + (i * (box_width + spacing))

            # Draw box with subtle shadow effect
            if concept_name == "Executive":
                # Subtle border
                draw.rectangle([box_x, start_y, box_x + box_width, start_y + box_height],
                             outline=accent_color, width=2)
            elif concept_name == "Bold":
                # Filled box with accent
                draw.rectangle([box_x, start_y, box_x + box_width, start_y + box_height],
                             fill=accent_color)
            elif concept_name == "Editorial":
                # Elegant frame
                draw.rectangle([box_x, start_y, box_x + box_width, start_y + box_height],
                             outline=text_color, width=1)
                draw.rectangle([box_x + 10, start_y + 10, box_x + box_width - 10, start_y + box_height - 10],
                             outline=accent_color, width=1)

            # Pillar label
            label_color = (255, 255, 255) if concept_name == "Bold" else accent_color
            draw.text((box_x + 30, start_y + 40), pillar_labels[i], fill=label_color, font=body_font_bold)

            # Content
            content_y = start_y + 120
            content_color = (255, 255, 255) if concept_name == "Bold" else text_color
            for item in pillar_content[i]:
                # Wrap text if needed
                words = item.split()
                lines = []
                current_line = []
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    bbox = draw.textbbox((0, 0), test_line, font=body_font)
                    if bbox[2] - bbox[0] < box_width - 60:
                        current_line.append(word)
                    else:
                        if current_line:
                            lines.append(' '.join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(' '.join(current_line))

                for line in lines:
                    draw.text((box_x + 30, content_y), f"• {line}", fill=content_color, font=body_font)
                    content_y += 50
                content_y += 20

    elif style == "timeline":
        # Weekly timeline layout
        draw.text((margin, margin), title_text, fill=text_color, font=title_font)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        activities = [
            "Set weekly goals",
            "Execute daily system",
            "Quality applications",
            "Execute + apply",
            "Review metrics",
            "Interview prep",
            "Plan next week"
        ]

        start_y = margin + 200
        day_height = 90

        for i, (day, activity) in enumerate(zip(days, activities)):
            y_pos = start_y + (i * day_height)

            # Day box
            if concept_name == "Bold":
                # Full-width color bar
                draw.rectangle([margin, y_pos, margin + 300, y_pos + 60], fill=accent_color)
                draw.text((margin + 20, y_pos + 10), day, fill=(255, 255, 255), font=body_font_bold)
            else:
                # Day label with accent
                draw.text((margin, y_pos), day, fill=accent_color, font=body_font_bold)

            # Activity description
            activity_x = margin + 350
            draw.text((activity_x, y_pos + 10), activity, fill=text_color, font=body_font)

            # Connecting line
            if i < len(days) - 1:
                if concept_name == "Editorial":
                    draw.line([margin + 20, y_pos + 70, margin + 20, y_pos + 90], fill=accent_color, width=2)
                else:
                    draw.line([margin + 150, y_pos + 70, margin + 150, y_pos + 90], fill=accent_color, width=3)

    else:
        # Default content slide
        draw.text((margin, margin), title_text, fill=text_color, font=title_font)

        y_offset = margin + 180
        for item in body_content:
            draw.text((margin, y_offset), f"• {item}", fill=text_color, font=body_font)
            y_offset += 70

    return img


# CONCEPT A: Executive Minimalism
def create_executive_concept():
    """Navy/charcoal + gold + white"""
    bg_color = (245, 245, 245)  # Light gray
    text_color = (26, 31, 46)  # Deep navy
    accent_color = (212, 175, 55)  # Gold

    slides = []

    # Slide 1 - Title
    img = create_slide(
        bg_color=text_color,  # Dark background for title
        text_color=(255, 255, 255),  # White text
        accent_color=accent_color,
        title_text="The Psychology of\nHigh-Ticket Job Searches",
        body_content=[],
        concept_name="Executive",
        slide_num=1,
        style="title"
    )
    slides.append(("ConceptA_Slide01.png", img))

    # Slide 15 - Reframing
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Reframing Exercise",
        body_content=[
            '"I\'m not qualified"',
            '"I need more experience"',
            '"They won\'t pay me that"',
            '"I bring unique value"',
            '"I have transferable skills"',
            '"I solve high-value problems"'
        ],
        concept_name="Executive",
        slide_num=15,
        style="compare"
    )
    slides.append(("ConceptA_Slide15.png", img))

    # Slide 20 - Confidence Framework
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Three Pillars of Career Confidence",
        body_content=[],
        concept_name="Executive",
        slide_num=20,
        style="framework"
    )
    slides.append(("ConceptA_Slide20.png", img))

    # Slide 50 - Weekly System
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Your Weekly Job Search Rhythm",
        body_content=[],
        concept_name="Executive",
        slide_num=50,
        style="timeline"
    )
    slides.append(("ConceptA_Slide50.png", img))

    return slides


# CONCEPT B: Bold & Energetic
def create_bold_concept():
    """Purple/navy + bright orange + white"""
    bg_color = (255, 255, 255)  # White
    text_color = (44, 62, 80)  # Dark blue-gray
    accent_color = (255, 107, 53)  # Bright orange

    slides = []

    # Slide 1 - Title
    img = create_slide(
        bg_color=(52, 73, 94),  # Navy background
        text_color=(255, 255, 255),
        accent_color=accent_color,
        title_text="The Psychology of\nHigh-Ticket Job Searches",
        body_content=[],
        concept_name="Bold",
        slide_num=1,
        style="title"
    )
    slides.append(("ConceptB_Slide01.png", img))

    # Slide 15 - Reframing
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Reframing Exercise",
        body_content=[
            '"I\'m not qualified"',
            '"I need more experience"',
            '"They won\'t pay me that"',
            '"I bring unique value"',
            '"I have transferable skills"',
            '"I solve high-value problems"'
        ],
        concept_name="Bold",
        slide_num=15,
        style="compare"
    )
    slides.append(("ConceptB_Slide15.png", img))

    # Slide 20 - Confidence Framework
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Three Pillars of Career Confidence",
        body_content=[],
        concept_name="Bold",
        slide_num=20,
        style="framework"
    )
    slides.append(("ConceptB_Slide20.png", img))

    # Slide 50 - Weekly System
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Your Weekly Job Search Rhythm",
        body_content=[],
        concept_name="Bold",
        slide_num=50,
        style="timeline"
    )
    slides.append(("ConceptB_Slide50.png", img))

    return slides


# CONCEPT C: Editorial Sophistication
def create_editorial_concept():
    """Navy + burgundy + cream + gold"""
    bg_color = (250, 248, 245)  # Cream
    text_color = (26, 31, 46)  # Deep navy
    accent_color = (128, 0, 32)  # Burgundy

    slides = []

    # Slide 1 - Title
    img = create_slide(
        bg_color=text_color,
        text_color=(250, 248, 245),
        accent_color=(212, 175, 55),  # Gold accent
        title_text="The Psychology of\nHigh-Ticket Job Searches",
        body_content=[],
        concept_name="Editorial",
        slide_num=1,
        style="title"
    )
    slides.append(("ConceptC_Slide01.png", img))

    # Slide 15 - Reframing
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Reframing Exercise",
        body_content=[
            '"I\'m not qualified"',
            '"I need more experience"',
            '"They won\'t pay me that"',
            '"I bring unique value"',
            '"I have transferable skills"',
            '"I solve high-value problems"'
        ],
        concept_name="Editorial",
        slide_num=15,
        style="compare"
    )
    slides.append(("ConceptC_Slide15.png", img))

    # Slide 20 - Confidence Framework
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Three Pillars of Career Confidence",
        body_content=[],
        concept_name="Editorial",
        slide_num=20,
        style="framework"
    )
    slides.append(("ConceptC_Slide20.png", img))

    # Slide 50 - Weekly System
    img = create_slide(
        bg_color=bg_color,
        text_color=text_color,
        accent_color=accent_color,
        title_text="Your Weekly Job Search Rhythm",
        body_content=[],
        concept_name="Editorial",
        slide_num=50,
        style="timeline"
    )
    slides.append(("ConceptC_Slide50.png", img))

    return slides


def main():
    print("Generating proof-of-concept designs...")

    # Create all three concepts
    all_slides = []
    all_slides.extend(create_executive_concept())
    all_slides.extend(create_bold_concept())
    all_slides.extend(create_editorial_concept())

    # Save individual PNG files
    for filename, img in all_slides:
        img.save(filename)
        print(f"Created: {filename}")

    print(f"\nTotal slides created: {len(all_slides)}")
    print("All PNG files saved successfully!")


if __name__ == "__main__":
    main()
