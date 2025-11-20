#!/usr/bin/env python3
"""
Active Offer Webinar v4.1 - Styled with v2.1 Design
Creates professional PNG slides at 1920x1080 resolution
Uses EXACT style specifications from v2.1
Extracts content from Webinar-Script-v4.1-Bold-Promise.md
"""

from playwright.sync_api import sync_playwright
import os
import re

# EXACT v2.1 COLOR PALETTE - DO NOT MODIFY
COLORS = {
    'primary': '#1a365d',      # Deep blue (for main titles)
    'secondary': '#2c5282',    # Medium blue (for h2)
    'accent': '#3182ce',       # Bright blue (for highlights/CTAs)
    'text_dark': '#1a202c',    # Almost black (body text)
    'text_light': '#ffffff',   # White
    'gray_light': '#e2e8f0',   # Light gray (boxes)
    'gray_medium': '#cbd5e0',  # Medium gray
    'gray_dark': '#4a5568',    # Dark gray (subheads)
    'success': '#38a169',      # Green for checkmarks
    'warning': '#e53e3e',      # Red for X marks
}

def create_html_template(content, bg_color='#ffffff', text_color='#1a202c'):
    """Creates base HTML template for slides with EXACT v2.1 styling"""
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            width: 1920px;
            height: 1080px;
            background: {bg_color};
            color: {text_color};
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 80px;
            overflow: hidden;
        }}

        .slide {{
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}

        .slide-left {{
            text-align: left;
            align-items: flex-start;
        }}

        h1 {{
            font-size: 96px;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 40px;
            color: {COLORS['primary']};
        }}

        h2 {{
            font-size: 72px;
            font-weight: 600;
            line-height: 1.3;
            margin-bottom: 30px;
            color: {COLORS['secondary']};
        }}

        h3 {{
            font-size: 56px;
            font-weight: 500;
            line-height: 1.4;
            margin-bottom: 24px;
            color: {COLORS['gray_dark']};
        }}

        p {{
            font-size: 42px;
            line-height: 1.6;
            margin-bottom: 20px;
            max-width: 1400px;
        }}

        .subhead {{
            font-size: 48px;
            color: {COLORS['gray_dark']};
            font-weight: 400;
            line-height: 1.5;
        }}

        .large-text {{
            font-size: 64px;
            font-weight: 600;
            line-height: 1.4;
            max-width: 1500px;
            margin: 40px 0;
        }}

        ul {{
            list-style: none;
            font-size: 42px;
            line-height: 1.8;
            text-align: left;
            max-width: 1400px;
        }}

        li {{
            margin-bottom: 24px;
            padding-left: 50px;
            position: relative;
        }}

        li:before {{
            content: "•";
            position: absolute;
            left: 0;
            color: {COLORS['accent']};
            font-weight: bold;
            font-size: 48px;
        }}

        .checkmark:before {{
            content: "✓";
            color: {COLORS['success']};
        }}

        .xmark:before {{
            content: "✗";
            color: {COLORS['warning']};
        }}

        .split {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            width: 100%;
            align-items: start;
        }}

        .split h3 {{
            margin-bottom: 30px;
            font-size: 48px;
        }}

        .split ul {{
            font-size: 36px;
        }}

        .split li {{
            margin-bottom: 20px;
        }}

        .box {{
            background: {COLORS['gray_light']};
            padding: 40px;
            border-radius: 12px;
            margin: 20px 0;
        }}

        .box-dark {{
            background: {COLORS['primary']};
            color: {COLORS['text_light']};
            padding: 40px;
            border-radius: 12px;
            margin: 20px 0;
        }}

        .number-stat {{
            font-size: 120px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin: 30px 0;
        }}

        .quote {{
            font-size: 48px;
            font-style: italic;
            line-height: 1.6;
            max-width: 1400px;
            padding: 40px;
            border-left: 8px solid {COLORS['accent']};
            background: {COLORS['gray_light']};
            border-radius: 8px;
            text-align: left;
        }}

        .cta {{
            background: {COLORS['accent']};
            color: {COLORS['text_light']};
            padding: 30px 60px;
            font-size: 56px;
            font-weight: 600;
            border-radius: 12px;
            margin: 40px 0;
            display: inline-block;
        }}

        .small-text {{
            font-size: 32px;
            color: {COLORS['gray_dark']};
            margin-top: 20px;
        }}

        .steps {{
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin: 40px 0;
        }}

        .step {{
            flex: 1;
            padding: 30px;
            text-align: center;
        }}

        .step-number {{
            font-size: 72px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 20px;
        }}

        .step-title {{
            font-size: 36px;
            font-weight: 600;
            color: {COLORS['primary']};
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def parse_markdown_to_slides(md_file_path):
    """Parse v4.1 markdown and extract ONLY audience-facing content"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    slides = []

    # Split by slide markers (### Slide ...) - capture slide number only
    # The pattern captures the slide number (with optional letters or sub-numbers) and ignores any title after the colon
    # Supports formats: 13, 13A, 13F, 31-1, 31-2, 88-1, 88-2, etc.
    slide_pattern = re.compile(r'### Slide ([\d]+[A-Z]?(?:-\d+)?)(?::[^\n]*)?\n(.*?)(?=### Slide [\d]+|$)', re.DOTALL)
    matches = slide_pattern.findall(content)

    for slide_num, slide_content in matches:
        lines = slide_content.strip().split('\n')
        clean_lines = []
        in_quotes = False

        for line in lines:
            line = line.strip()

            # REMOVE all meta-content that should NOT appear on slides

            # Skip Visual Suggestions and Delivery Notes
            if line.startswith('**[Visual Suggestion:') or line.startswith('**[Delivery Note:'):
                continue

            # Skip closing brackets for multi-line notes
            if line == '**' or line.startswith(']**') or line.endswith(']**'):
                continue

            # Skip ANY section headers (starting with ##)
            if line.startswith('##'):
                continue

            # Skip horizontal rules
            if line == '---':
                continue

            # Skip empty lines
            if not line:
                continue

            # Skip lines that contain structural instructions
            if line.startswith('**Purpose:') or line.startswith('**Replace With:') or line.startswith('Purpose:'):
                continue

            # Skip parenthetical notes like "(THE HERO MOMENT)" or "(Slides 51-75)"
            if line.startswith('(') and line.endswith(')'):
                continue

            # Process "Title Slide:" prefix - extract only the title text
            if line.startswith('Title Slide:'):
                # Remove "Title Slide:" prefix and extract quoted content
                title_text = line.replace('Title Slide:', '').strip()
                # Remove ** markdown bold markers if present
                title_text = title_text.strip('*')
                # Remove quotes if present
                title_text = title_text.strip('"')
                clean_lines.append(title_text)
                continue

            # Extract content from quotes - this is the actual slide text
            if line.startswith('"') and line.endswith('"'):
                # Remove quotes and clean up markdown bold markers
                text = line.strip('"')
                # Remove ** markdown bold markers but keep the text
                text = text.replace('**', '')
                clean_lines.append(text)
                continue

            # Handle multi-line quoted content
            if line.startswith('"'):
                text = line.lstrip('"')
                text = text.replace('**', '')
                clean_lines.append(text)
                in_quotes = True
                continue

            if line.endswith('"'):
                text = line.rstrip('"')
                text = text.replace('**', '')
                clean_lines.append(text)
                in_quotes = False
                continue

            # If we're inside quoted content, include the line
            if in_quotes:
                # Clean up markdown bold markers
                text = line.replace('**', '')
                clean_lines.append(text)
                continue

            # Skip lines that start with ** (these are bold metadata)
            if line.startswith('**'):
                continue

            # Only include specific markdown patterns outside quotes
            # - Markdown headers (for structure slides)
            # - Bullet points with - or *
            if line.startswith('#') or line.startswith('-') or line.startswith('*'):
                clean_lines.append(line)
                continue

        if clean_lines:
            slides.append({
                'num': slide_num,
                'content': '\n'.join(clean_lines)
            })

    return slides

def content_to_html(content):
    """Convert markdown content to HTML with v2.1 styling"""
    lines = content.split('\n')

    # Detect slide type based on content
    has_bullets = any(line.strip().startswith('-') or line.strip().startswith('*') for line in lines)
    is_title_slide = len(lines) <= 3 and not has_bullets
    is_large_text = len(content) < 200 and not has_bullets and not is_title_slide

    html_parts = []

    if is_title_slide:
        # Title slide - centered
        html_parts.append('<div class="slide">')
        for line in lines:
            line = line.strip()
            if line.startswith('**') and line.endswith('**'):
                # Bold subtitle
                text = line.strip('*')
                html_parts.append(f'<p class="subhead">{text}</p>')
            elif line:
                # Main title
                html_parts.append(f'<h1 style="color: {COLORS["primary"]};">{line}</h1>')
        html_parts.append('</div>')

    elif is_large_text:
        # Large quote/statement slide
        html_parts.append('<div class="slide">')
        for line in lines:
            line = line.strip()
            if line.startswith('**') and line.endswith('**'):
                text = line.strip('*')
                html_parts.append(f'<p class="large-text" style="font-weight: 700; color: {COLORS["primary"]};">{text}</p>')
            elif line:
                html_parts.append(f'<p class="large-text">{line}</p>')
        html_parts.append('</div>')

    elif has_bullets:
        # Bullet list slide - left aligned
        html_parts.append('<div class="slide slide-left">')
        in_list = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('#'):
                # Heading
                level = len(line) - len(line.lstrip('#'))
                text = line.lstrip('#').strip()
                if level == 1:
                    html_parts.append(f'<h1>{text}</h1>')
                elif level == 2:
                    html_parts.append(f'<h2>{text}</h2>')
                else:
                    html_parts.append(f'<h3>{text}</h3>')

            elif line.startswith('-') or line.startswith('*'):
                # Bullet point
                if not in_list:
                    html_parts.append('<ul>')
                    in_list = True

                text = line.lstrip('-*').strip()

                # Check for checkmark or xmark
                if '✓' in text or '(checkmark)' in text:
                    html_parts.append(f'<li class="checkmark">{text.replace("✓", "").replace("(checkmark)", "").strip()}</li>')
                elif '✗' in text or '(xmark)' in text:
                    html_parts.append(f'<li class="xmark">{text.replace("✗", "").replace("(xmark)", "").strip()}</li>')
                else:
                    html_parts.append(f'<li>{text}</li>')

            else:
                # Regular text
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False

                if line.startswith('**') and line.endswith('**'):
                    text = line.strip('*')
                    html_parts.append(f'<h2>{text}</h2>')
                else:
                    html_parts.append(f'<p>{line}</p>')

        if in_list:
            html_parts.append('</ul>')

        html_parts.append('</div>')

    else:
        # Standard content slide
        html_parts.append('<div class="slide">')

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                text = line.lstrip('#').strip()
                if level == 1:
                    html_parts.append(f'<h1>{text}</h1>')
                elif level == 2:
                    html_parts.append(f'<h2>{text}</h2>')
                else:
                    html_parts.append(f'<h3>{text}</h3>')
            elif line.startswith('**') and line.endswith('**'):
                text = line.strip('*')
                html_parts.append(f'<p class="large-text" style="font-weight: 700; color: {COLORS["primary"]};">{text}</p>')
            else:
                html_parts.append(f'<p>{line}</p>')

        html_parts.append('</div>')

    return '\n'.join(html_parts)

def create_image_placeholder_html(description):
    """Create HTML for image placeholder slide with v2.1 styling"""
    return f"""
<div class="slide">
    <div style="
        border: 8px dashed {COLORS['accent']};
        padding: 100px 80px;
        border-radius: 20px;
        background: {COLORS['gray_light']};
        max-width: 1400px;
        text-align: center;
    ">
        <p style="
            font-size: 64px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 40px;
            letter-spacing: 2px;
        ">[INSERT IMAGE]</p>
        <p style="
            font-size: 42px;
            line-height: 1.6;
            color: {COLORS['gray_dark']};
            max-width: 1000px;
            margin: 0 auto;
        ">{description}</p>
    </div>
</div>
"""

def create_combo_slide_html(slide_data):
    """Generate HTML for combo text+image slides based on layout type"""
    layout_type = slide_data['type']

    if layout_type == 'narrative_illustration':
        return create_narrative_illustration(slide_data)
    elif layout_type == 'framework_diagram':
        return create_framework_diagram(slide_data)
    elif layout_type == 'data_visualization':
        return create_data_visualization(slide_data)
    elif layout_type == 'before_after':
        return create_before_after_comparison(slide_data)
    else:
        # Fallback to simple placeholder
        return create_image_placeholder_html(slide_data.get('image_desc', ''))

def create_narrative_illustration(data):
    """Layout: Image placeholder on left/right, all text on opposite side"""
    top_text = data.get('top_text', '')
    subtitle = data.get('subtitle', '')
    bottom_text = data.get('bottom_text', '')
    bullets = data.get('bullets', [])
    corners = data.get('corners', [])
    image_desc = data.get('image_desc', '')
    image_side = data.get('image_side', 'left')  # 'left' or 'right'

    html = '<div class="slide" style="flex-direction: row; align-items: stretch; justify-content: space-between; gap: 60px;">'

    # Image placeholder box
    image_html = f'''
    <div style="
        border: 6px dashed {COLORS['accent']};
        padding: 60px 40px;
        border-radius: 16px;
        background: {COLORS['gray_light']};
        flex: 0 0 45%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 700px;
    ">
        <p style="
            font-size: 48px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 20px;
            letter-spacing: 1px;
        ">[IMAGE]</p>
        <p style="
            font-size: 24px;
            line-height: 1.5;
            color: {COLORS['gray_dark']};
            text-align: center;
        ">{image_desc}</p>
    </div>
    '''

    # Text content box
    text_html = '<div style="flex: 1; display: flex; flex-direction: column; justify-content: center; text-align: left;">'

    if top_text:
        text_html += f'<h2 style="margin-bottom: 30px; line-height: 1.3;">{top_text}</h2>'
    if subtitle:
        text_html += f'<p class="subhead" style="margin-bottom: 30px;">{subtitle}</p>'

    # Bullets if present
    if bullets:
        text_html += '<ul style="margin: 30px 0; font-size: 38px; line-height: 1.8;">'
        for bullet in bullets:
            text_html += f'<li>{bullet}</li>'
        text_html += '</ul>'

    # Corners layout if present
    if corners:
        text_html += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0;">'
        for corner in corners:
            text_html += f'<p style="font-size: 32px; color: {COLORS["gray_dark"]};">{corner}</p>'
        text_html += '</div>'

    if bottom_text:
        text_html += f'<p style="font-size: 44px; font-weight: 600; line-height: 1.4; color: {COLORS["primary"]}; margin-top: 40px;">{bottom_text}</p>'

    text_html += '</div>'

    # Assemble based on image_side
    if image_side == 'right':
        html += text_html + image_html
    else:
        html += image_html + text_html

    html += '</div>'
    return html

def create_framework_diagram(data):
    """Layout: Image placeholder on left/right, title and takeaway text on opposite side"""
    title = data.get('title', '')
    bottom_text = data.get('bottom_text', '')
    metric = data.get('metric', '')
    image_desc = data.get('image_desc', '')
    image_side = data.get('image_side', 'left')

    html = '<div class="slide" style="flex-direction: row; align-items: stretch; justify-content: space-between; gap: 60px;">'

    # Image placeholder box
    image_html = f'''
    <div style="
        border: 6px dashed {COLORS['accent']};
        padding: 60px 40px;
        border-radius: 16px;
        background: {COLORS['gray_light']};
        flex: 0 0 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 700px;
    ">
        <p style="
            font-size: 48px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 20px;
            letter-spacing: 1px;
        ">[FRAMEWORK]</p>
        <p style="
            font-size: 24px;
            line-height: 1.5;
            color: {COLORS['gray_dark']};
            text-align: center;
        ">{image_desc}</p>
    </div>
    '''

    # Text content box
    text_html = '<div style="flex: 1; display: flex; flex-direction: column; justify-content: center; text-align: left;">'

    if title:
        text_html += f'<h2 style="margin-bottom: 40px; line-height: 1.3; font-size: 56px;">{title}</h2>'

    if metric:
        text_html += f'<p style="font-size: 96px; font-weight: 700; color: {COLORS["accent"]}; margin: 40px 0;">{metric}</p>'

    if bottom_text:
        text_html += f'<p style="font-size: 42px; font-weight: 600; line-height: 1.4; color: {COLORS["primary"]}; margin-top: 40px;">{bottom_text}</p>'

    text_html += '</div>'

    # Assemble based on image_side
    if image_side == 'right':
        html += text_html + image_html
    else:
        html += image_html + text_html

    html += '</div>'
    return html

def create_data_visualization(data):
    """Layout: Image placeholder on left/right, headline/metric/text on opposite side"""
    headline = data.get('headline', '')
    metric = data.get('metric', '')
    subtitle = data.get('subtitle', '')
    bottom_text = data.get('bottom_text', '')
    image_desc = data.get('image_desc', '')
    image_side = data.get('image_side', 'left')

    html = '<div class="slide" style="flex-direction: row; align-items: stretch; justify-content: space-between; gap: 60px;">'

    # Image placeholder box
    image_html = f'''
    <div style="
        border: 6px dashed {COLORS['accent']};
        padding: 60px 40px;
        border-radius: 16px;
        background: {COLORS['gray_light']};
        flex: 0 0 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 700px;
    ">
        <p style="
            font-size: 48px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 20px;
            letter-spacing: 1px;
        ">[DATA VIZ]</p>
        <p style="
            font-size: 24px;
            line-height: 1.5;
            color: {COLORS['gray_dark']};
            text-align: center;
        ">{image_desc}</p>
    </div>
    '''

    # Text content box
    text_html = '<div style="flex: 1; display: flex; flex-direction: column; justify-content: center; text-align: left;">'

    if headline:
        text_html += f'<h1 style="margin-bottom: 30px; font-size: 72px; line-height: 1.2;">{headline}</h1>'
    if subtitle:
        text_html += f'<p class="subhead" style="margin-bottom: 30px;">{subtitle}</p>'

    if metric:
        text_html += f'<p style="font-size: 96px; font-weight: 700; color: {COLORS["accent"]}; margin: 40px 0; line-height: 1.1;">{metric}</p>'

    if bottom_text:
        text_html += f'<p style="font-size: 38px; font-weight: 500; line-height: 1.5; color: {COLORS["text_dark"]}; margin-top: 30px;">{bottom_text}</p>'

    text_html += '</div>'

    # Assemble based on image_side
    if image_side == 'right':
        html += text_html + image_html
    else:
        html += image_html + text_html

    html += '</div>'
    return html

def create_before_after_comparison(data):
    """Layout: Two-column comparison (left vs right) with title/subtitle at top and bottom statement"""
    title = data.get('title', '')
    top_text = data.get('top_text', '')
    subtitle = data.get('subtitle', '')
    left_title = data.get('left_title', '')
    left_text = data.get('left_text', '')
    left_items = data.get('left_items', [])
    right_title = data.get('right_title', '')
    right_text = data.get('right_text', '')
    right_items = data.get('right_items', [])
    bottom_text = data.get('bottom_text', '')
    image_desc = data.get('image_desc', '')

    html = '<div class="slide" style="flex-direction: column; justify-content: center;">'

    # Title/Top text
    if title:
        html += f'<h1 style="margin-bottom: 30px; font-size: 84px; text-align: center;">{title}</h1>'
    if top_text:
        html += f'<h2 style="margin-bottom: 40px; font-size: 56px; text-align: center;">{top_text}</h2>'
    if subtitle:
        html += f'<p class="subhead" style="margin-bottom: 40px; text-align: center;">{subtitle}</p>'

    # Split comparison or image placeholder
    if left_title or left_items or right_title or right_items:
        # Two column comparison layout
        html += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; margin: 40px 0; align-items: start;">'

        # Left side
        html += '<div style="text-align: left;">'
        if left_title:
            html += f'<h3 style="color: {COLORS["success"]}; margin-bottom: 30px; font-size: 42px;">{left_title}</h3>'
        if left_items:
            html += '<ul style="font-size: 38px; line-height: 1.8;">'
            for item in left_items:
                html += f'<li>{item}</li>'
            html += '</ul>'
        if left_text:
            html += f'<p style="font-size: 38px; line-height: 1.6;">{left_text}</p>'
        html += '</div>'

        # Right side
        html += '<div style="text-align: left;">'
        if right_title:
            html += f'<h3 style="color: {COLORS["warning"]}; margin-bottom: 30px; font-size: 42px;">{right_title}</h3>'
        if right_items:
            html += '<ul style="font-size: 38px; line-height: 1.8;">'
            for item in right_items:
                html += f'<li>{item}</li>'
            html += '</ul>'
        if right_text:
            html += f'<p style="font-size: 38px; line-height: 1.6;">{right_text}</p>'
        html += '</div>'

        html += '</div>'
    else:
        # Image placeholder if no split content
        html += f'''
        <div style="
            border: 6px dashed {COLORS['accent']};
            padding: 80px 60px;
            border-radius: 16px;
            background: {COLORS['gray_light']};
            margin: 40px auto;
            max-width: 1200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 400px;
        ">
            <p style="
                font-size: 48px;
                font-weight: 700;
                color: {COLORS['accent']};
                margin-bottom: 20px;
                letter-spacing: 1px;
            ">[COMPARISON]</p>
            <p style="
                font-size: 24px;
                line-height: 1.5;
                color: {COLORS['gray_dark']};
                text-align: center;
            ">{image_desc}</p>
        </div>
        '''

    # Bottom transformation statement
    if bottom_text:
        html += f'<p style="margin-top: 50px; font-weight: 700; text-align: center; color: {COLORS["primary"]}; font-size: 48px; line-height: 1.3;">{bottom_text}</p>'

    html += '</div>'
    return html

# Define combo slides with text + image placeholders
# Each slide has: type (layout category), text content, and image description
COMBO_SLIDES = {
    '12-img': {
        'type': 'narrative_illustration',
        'top_text': '10 Years. $130K. Stuck.',
        'subtitle': 'AT&T - 2021',
        'image_desc': 'Before state: AT&T office environment. "$130K after 10 years" text overlay. Stressed professional at desk.'
    },
    '13B-img': {
        'type': 'narrative_illustration',
        'top_text': '90 Days From Now...',
        'bottom_text': 'You\'re Reviewing THREE Job Offers',
        'image_desc': 'Clean, organized home workspace scene. Morning light streaming in. Quality coffee mug. Laptop showing multiple opportunity tabs.'
    },
    '13D-img': {
        'type': 'narrative_illustration',
        'top_text': 'YOU Get to Choose:',
        'bullets': ['Company Culture', 'Role Fit', 'Compensation', 'Work-Life Balance'],
        'image_desc': 'Split screen showing: company culture icons, role descriptions, compensation packages, work-life balance symbols.'
    },
    '13F-img': {
        'type': 'narrative_illustration',
        'top_text': 'This Isn\'t Fantasy. This Is Real.',
        'bottom_text': 'And I\'ll Show You Exactly How',
        'image_desc': 'Before/After transformation visual. Left: stressed person at cluttered desk. Right: confident person reviewing multiple offers.'
    },
    '22-img': {
        'type': 'data_visualization',
        'headline': '10 Years of Hard Work',
        'metric': '$65K → $130K',
        'bottom_text': 'But I Hit a Ceiling...',
        'image_desc': 'Timeline graphic: 2011-2021. AT&T logo. Income progression visualization showing growth plateau.'
    },
    '23-img': {
        'type': 'data_visualization',
        'headline': '$130K = The Ceiling',
        'bottom_text': 'No Matter How Hard I Worked',
        'image_desc': 'Income ceiling graph. Growth line plateauing. Visual representation of career plateau.'
    },
    '24-img': {
        'type': 'narrative_illustration',
        'top_text': 'And It Wasn\'t Enough',
        'corners': ['Debt Piling Up', 'Missing Family Time', '60-Hour Weeks', 'Career Stuck'],
        'image_desc': 'Four-panel pain point visual: debt bills stack, missed family moments, long work hours clock, career stagnation barrier.'
    },
    '26-img': {
        'type': 'narrative_illustration',
        'top_text': 'Then I Overheard Two Coworkers Talking...',
        'bottom_text': 'Same Skills as Me. Different Company. 3× the Income.',
        'image_desc': 'Office environment. Two silhouetted colleagues. Speech bubble: "$400,000". Shocked listener reaction.'
    },
    '37-img': {
        'type': 'framework_diagram',
        'title': 'The 3 Positioning Factors',
        'bottom_text': 'Master These → Control Your Income',
        'image_desc': 'Three architectural pillars. Left: "WHO - Which Companies Pay More". Center: "WHICH - Roles & Comp Structure". Right: "HOW - Strategic Positioning". Foundation labeled "STRATEGIC POSITIONING".'
    },
    '46-img': {
        'type': 'narrative_illustration',
        'top_text': 'Sound Familiar?',
        'image_desc': 'Thought bubbles surrounding central figure: "Not qualified enough", "No connections", "Don\'t have the background", "This won\'t work for me".'
    },
    '48-img': {
        'type': 'before_after',
        'top_text': 'Here\'s What You Need to Hear...',
        'left_title': 'YOU ALREADY HAVE:',
        'left_items': ['✓ Experience', '✓ Skills', '✓ Track Record'],
        'right_title': 'YOU DON\'T NEED:',
        'right_items': ['✗ MBA', '✗ Connections', '✗ More Skills'],
        'bottom_text': 'You\'re Not Under-Qualified. You\'re Under-POSITIONED.',
        'image_desc': 'Two-column comparison visual with checkmarks and X marks.'
    },
    '51-img': {
        'type': 'data_visualization',
        'headline': 'Week 3: Results',
        'bottom_text': '3 Interviews Scheduled',
        'image_desc': 'Success timeline. Week 1-3 progression. Google, Amazon, Salesforce logos with checkmarks.'
    },
    '56-img': {
        'type': 'narrative_illustration',
        'top_text': 'The Doubts Came Back...',
        'bottom_text': 'Have You Felt This Way?',
        'image_desc': 'Impostor syndrome visualization. Central defeated figure. Surrounding thought bubbles with doubt statements.'
    },
    '59-img': {
        'type': 'narrative_illustration',
        'top_text': 'The Decision:',
        'bottom_text': 'This Time, I\'ll Be Prepared',
        'subtitle': 'Positioning = Preparation',
        'image_desc': 'Determined professional at organized desk. Research materials spread out. Preparation checklist visible.'
    },
    '64-img': {
        'type': 'before_after',
        'title': 'YOU ARE QUALIFIED',
        'subtitle': 'The Problem Isn\'t Your Skills... It\'s Your Positioning',
        'image_desc': 'Large bold text with checklist showing Experience ✓, Skills ✓, Results ✓.'
    },
    '66-img': {
        'type': 'framework_diagram',
        'title': 'You Don\'t Need NEW Skills. You Need to REPOSITION Your Existing Skills.',
        'bottom_text': 'It\'s Not About HAVING More. It\'s About POSITIONING What You Have.',
        'image_desc': 'Skills translation matrix. Two columns with arrows. Left: "Your Current Skills". Right: "How They Position for $300K+ Roles". Shows examples like "Telesales Experience → Multi-channel sales strategy expertise".'
    },
    '73-img': {
        'type': 'data_visualization',
        'headline': 'The Pattern Is Clear',
        'bottom_text': 'Same Skills • Better Positioning • Repeatable Results',
        'image_desc': 'Three case studies side-by-side showing repeatable pattern labeled "SAME SKILLS, BETTER POSITIONING".'
    },
    '75-img': {
        'type': 'narrative_illustration',
        'top_text': 'But What About...',
        'bottom_text': 'Can This Really Work for YOU?',
        'image_desc': 'External objections thought cloud. Multiple bubbles: "No time", "Full-time job", "Family responsibilities", "Can\'t quit", "Too busy".'
    },
    '84-img': {
        'type': 'data_visualization',
        'headline': 'The 5-Day Experiment',
        'metric': '30 min/day × 5 days = 3 INTERVIEWS',
        'bottom_text': 'Same System Still Works Today',
        'image_desc': '5-day calendar with daily 30-min blocks. Leading to "Week 2: THREE INTERVIEWS SCHEDULED". Google, Amazon, Salesforce logos with checkmarks.'
    },
    '86-img': {
        'type': 'framework_diagram',
        'title': 'Reverse Attraction',
        'bottom_text': 'Stop Chasing. Start Attracting.',
        'image_desc': 'Process reversal diagram showing arrows. Traditional: You → Company (applicant). Reverse: Company → You (recruitment). "FLIP THE SCRIPT" messaging.'
    },
    '93-img': {
        'type': 'data_visualization',
        'headline': 'Darrell\'s First Success',
        'metric': '+$90K Raise',
        'subtitle': '$100K → $190K',
        'bottom_text': '30 Min/Day • While Employed • Weeks, Not Years',
        'image_desc': 'Transformation timeline showing income jump with visual progression.'
    },
    '96-img': {
        'type': 'data_visualization',
        'headline': 'The System Works',
        'bottom_text': '30 Min/Day • Employed • $75K+ Raises',
        'image_desc': 'Three success stories comparison. Each showing "30 Min/Day" + "While Employed" + "$75K-$125K Raises". "PROVEN SYSTEM" label.'
    },
    '101-img': {
        'type': 'narrative_illustration',
        'top_text': '1 Year From Now',
        'metric': '$75K-$125K More Annually',
        'image_desc': 'One-year transformation timeline. "Today" vs "1 Year from Now" side-by-side comparison. Dollar amounts and lifestyle improvements.'
    },
    '102-img': {
        'type': 'before_after',
        'left_text': 'You at 4:45 PM • Dinner with Family',
        'right_text': 'Old Colleagues • Still Working',
        'bottom_text': 'Better Position = Better Life',
        'image_desc': 'Split lifestyle scene. Left: 4:45 PM clock, closed laptop, family dinner. Right: colleagues stressed, working late.'
    },
    '110-img': {
        'type': 'framework_diagram',
        'title': 'Total Program Value',
        'metric': '$50,500',
        'image_desc': 'Value stack calculator. All seven components listed with individual values. Grand total prominently displayed. Visual stack building effect.'
    },
    '126-img': {
        'type': 'narrative_illustration',
        'headline': '15 Spots This Month',
        'bottom_text': 'Limited Availability • Book Your Call Today',
        'image_desc': 'Scarcity visual with countdown timer or limited slot indicators. Urgency call-to-action.'
    },
    '139-img': {
        'type': 'data_visualization',
        'headline': 'Day 1 → Day 45',
        'bottom_text': 'Your First Interview (They Recruited YOU)',
        'subtitle': 'This Is Positioning in Action',
        'image_desc': '45-day timeline. "Day 1: Strategy Call" → "Day 45: First Interview". Confident candidate with engaged interviewer. Checkmark: "They Recruited YOU."'
    }
}

def generate_slides():
    """Generate all v4.1 slides with v2.1 styling"""
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/Webinar-v4.1-Slides-Styled"
    md_file = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/Webinar-Script-v4.1-Bold-Promise.md"

    print(f"Starting slide generation for v4.1 with v2.1 styling...")
    print(f"Output directory: {output_dir}")
    print(f"Source markdown: {md_file}")
    print(f"\nExtracting slides from markdown...")

    # Parse markdown to get slides
    slides = parse_markdown_to_slides(md_file)

    print(f"\n✓ Found {len(slides)} slides in markdown")
    print(f"\nGenerating PNG slides with EXACT v2.1 styling...")
    print(f"  - Colors: Primary {COLORS['primary']}, Secondary {COLORS['secondary']}, Accent {COLORS['accent']}")
    print(f"  - Typography: System fonts, 96px titles, 72px h2, 42px body")
    print(f"  - Layout: 1920x1080, 80px padding, centered/left-aligned as needed")
    print(f"\n")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Generate regular content slides
        for i, slide_data in enumerate(slides, 1):
            slide_num = slide_data['num']
            content = slide_data['content']

            # Convert content to HTML
            html_content = content_to_html(content)
            full_html = create_html_template(html_content)

            # Set content
            page.set_content(full_html)

            # Wait for fonts and rendering
            page.wait_for_timeout(500)

            # Take screenshot
            output_path = os.path.join(output_dir, f"slide-{slide_num}.png")
            page.screenshot(path=output_path, full_page=False)

            print(f"Generated slide {slide_num} ({i}/{len(slides)})")

        # Generate combo text+image slides
        print(f"\n\nGenerating {len(COMBO_SLIDES)} combo text+image slides...")
        combo_count = 0
        for slide_id, slide_data in COMBO_SLIDES.items():
            combo_count += 1

            # Create combo slide HTML
            html_content = create_combo_slide_html(slide_data)
            full_html = create_html_template(html_content)

            # Set content
            page.set_content(full_html)

            # Wait for fonts and rendering
            page.wait_for_timeout(500)

            # Take screenshot
            output_path = os.path.join(output_dir, f"slide-{slide_id}.png")
            page.screenshot(path=output_path, full_page=False)

            layout_type = slide_data.get('type', 'unknown')
            print(f"Generated combo slide {slide_id} ({layout_type}) - {combo_count}/{len(COMBO_SLIDES)}")

        browser.close()

    total_slides = len(slides) + len(COMBO_SLIDES)
    print(f"\n✓ All {total_slides} slides generated successfully!")
    print(f"  - {len(slides)} content slides")
    print(f"  - {len(COMBO_SLIDES)} combo text+image slides")
    print(f"✓ Location: {output_dir}")
    print(f"\n✓ Style verification:")
    print(f"  - EXACT v2.1 color palette applied")
    print(f"  - EXACT v2.1 typography specs applied")
    print(f"  - EXACT v2.1 layout dimensions applied")
    print(f"  - v4.1 content with v2.1 visual identity")
    print(f"\n✓ Combo slide layouts:")
    print(f"  - Narrative Illustration: Context + image + emotional hook")
    print(f"  - Framework Diagram: Title + diagram + key takeaway")
    print(f"  - Data Visualization: Headline + data + key metric")
    print(f"  - Before/After: Split comparison + transformation statement")
    print(f"  - All 27 slides now have integrated text + image placeholders")
    print(f"\nSlides are ready for review!")

if __name__ == "__main__":
    generate_slides()
