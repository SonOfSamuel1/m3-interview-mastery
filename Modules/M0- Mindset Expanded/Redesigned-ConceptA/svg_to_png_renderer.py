"""
SVG to PNG Renderer for PIL Integration
Converts SVG graphics to PNG format that can be composited onto PIL images
Uses cairosvg for high-quality SVG rendering
"""

import io
from PIL import Image

try:
    import cairosvg
    CAIROSVG_AVAILABLE = True
except ImportError:
    CAIROSVG_AVAILABLE = False
    print("Warning: cairosvg not installed. SVG rendering will be limited.")
    print("Install with: pip install cairosvg")


def svg_to_pil_image(svg_string, scale=1.0):
    """
    Convert SVG string to PIL Image object

    Args:
        svg_string: SVG content as string
        scale: Scaling factor for rendering (default 1.0)

    Returns:
        PIL Image object with transparent background
    """
    if not CAIROSVG_AVAILABLE:
        # Fallback: create a placeholder image
        return create_placeholder_image()

    try:
        # Convert SVG to PNG bytes
        png_bytes = cairosvg.svg2png(
            bytestring=svg_string.encode('utf-8'),
            scale=scale
        )

        # Load PNG bytes into PIL Image
        png_image = Image.open(io.BytesIO(png_bytes))

        # Ensure RGBA mode for transparency
        if png_image.mode != 'RGBA':
            png_image = png_image.convert('RGBA')

        return png_image

    except Exception as e:
        print(f"Error rendering SVG: {e}")
        return create_placeholder_image()


def create_placeholder_image(size=100):
    """Create a simple placeholder when SVG rendering fails"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    return img


def composite_svg_on_image(base_image, svg_string, position, size=None, scale=1.0):
    """
    Composite SVG graphic onto a PIL image

    Args:
        base_image: PIL Image to composite onto
        svg_string: SVG content as string
        position: Tuple (x, y) for top-left corner of SVG
        size: Optional tuple (width, height) to resize SVG
        scale: Scaling factor for SVG rendering

    Returns:
        Modified PIL Image with SVG composited
    """
    # Convert SVG to PIL Image
    svg_image = svg_to_pil_image(svg_string, scale=scale)

    # Resize if size specified
    if size:
        svg_image = svg_image.resize(size, Image.Resampling.LANCZOS)

    # Composite onto base image
    base_image.paste(svg_image, position, svg_image)

    return base_image


def create_icon_with_label(svg_func, label, font, icon_size=80, text_color=(26, 31, 46),
                           icon_color="#D4AF37", canvas_width=300, spacing=20):
    """
    Create a composite image with an icon and label below it

    Args:
        svg_func: Function that generates SVG string
        label: Text label for the icon
        font: PIL ImageFont for the label
        icon_size: Size of the icon
        text_color: RGB tuple for text color
        icon_color: Hex color for icon
        canvas_width: Width of the canvas
        spacing: Space between icon and label

    Returns:
        PIL Image with icon and label
    """
    from PIL import ImageDraw

    # Generate SVG
    svg_string = svg_func(size=icon_size, color=icon_color)

    # Convert to PIL Image
    icon_image = svg_to_pil_image(svg_string, scale=2.0)

    # Ensure correct size
    if icon_image.size != (icon_size, icon_size):
        icon_image = icon_image.resize((icon_size, icon_size), Image.Resampling.LANCZOS)

    # Calculate text size
    temp_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(temp_img)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Create canvas
    canvas_height = icon_size + spacing + text_height + 20
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Center icon
    icon_x = (canvas_width - icon_size) // 2
    canvas.paste(icon_image, (icon_x, 0), icon_image)

    # Center text below icon
    text_x = (canvas_width - text_width) // 2
    text_y = icon_size + spacing
    draw.text((text_x, text_y), label, fill=text_color, font=font)

    return canvas


def render_svg_grid(svg_functions, labels, columns=3, icon_size=80, spacing=40,
                   font=None, icon_color="#D4AF37"):
    """
    Render multiple SVG icons in a grid layout

    Args:
        svg_functions: List of SVG generator functions
        labels: List of labels for each icon
        columns: Number of columns in grid
        icon_size: Size of each icon
        spacing: Space between icons
        font: PIL ImageFont for labels
        icon_color: Hex color for icons

    Returns:
        PIL Image with icon grid
    """
    from PIL import ImageDraw, ImageFont

    if font is None:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
        except:
            font = ImageFont.load_default()

    # Calculate grid dimensions
    rows = (len(svg_functions) + columns - 1) // columns

    # Calculate cell size (icon + label)
    cell_width = icon_size + spacing
    cell_height = icon_size + 60  # Extra space for label

    # Create canvas
    canvas_width = columns * cell_width + spacing
    canvas_height = rows * cell_height + spacing
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    # Render each icon
    for i, (svg_func, label) in enumerate(zip(svg_functions, labels)):
        row = i // columns
        col = i % columns

        x = col * cell_width + spacing
        y = row * cell_height + spacing

        # Generate and composite SVG
        svg_string = svg_func(size=icon_size, color=icon_color)
        composite_svg_on_image(canvas, svg_string, (x, y), scale=2.0)

        # Add label
        bbox = draw.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = x + (icon_size - text_width) // 2
        text_y = y + icon_size + 10
        draw.text((text_x, text_y), label, fill=(26, 31, 46), font=font)

    return canvas


# Alternative simple rendering for when cairosvg is not available
def simple_geometric_shape(shape_type='circle', size=80, color=(212, 175, 55)):
    """
    Create simple geometric shapes as PIL images (fallback when SVG rendering unavailable)

    Args:
        shape_type: 'circle', 'square', 'triangle', 'diamond'
        size: Size of the shape
        color: RGB tuple for color

    Returns:
        PIL Image with geometric shape
    """
    from PIL import ImageDraw

    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    padding = 10

    if shape_type == 'circle':
        draw.ellipse([padding, padding, size-padding, size-padding], fill=color)
    elif shape_type == 'square':
        draw.rectangle([padding, padding, size-padding, size-padding], fill=color)
    elif shape_type == 'triangle':
        points = [(size//2, padding), (size-padding, size-padding), (padding, size-padding)]
        draw.polygon(points, fill=color)
    elif shape_type == 'diamond':
        points = [(size//2, padding), (size-padding, size//2), (size//2, size-padding), (padding, size//2)]
        draw.polygon(points, fill=color)

    return img


if __name__ == "__main__":
    # Test SVG rendering
    from svg_graphics_library import create_lightbulb_icon, create_target_icon

    print("Testing SVG to PNG rendering...")

    # Test basic conversion
    svg = create_lightbulb_icon(size=100, color="#D4AF37")
    img = svg_to_pil_image(svg, scale=2.0)

    if img:
        img.save("test_lightbulb.png")
        print("Created test_lightbulb.png")

    # Test geometric fallback
    fallback = simple_geometric_shape('circle', size=80, color=(212, 175, 55))
    fallback.save("test_fallback_circle.png")
    print("Created test_fallback_circle.png")

    print(f"CairoSVG available: {CAIROSVG_AVAILABLE}")
