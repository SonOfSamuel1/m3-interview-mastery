"""
STARTUP PRESENTATION PDF COMPILER
==================================
Compiles all 57 startup-style slides into a single PDF.

This script:
1. Collects all slide-XX-startup.png files (slides 01-57)
2. Compiles them into a single PDF in sequential order
3. Outputs: M0-Mindset-Module-STARTUP-STYLE.pdf

Author: Claude Code
Version: 1.0
"""

from PIL import Image
import os

def compile_startup_slides_to_pdf():
    """Compile all startup-style slides into a PDF."""

    # Directory containing the slides
    base_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M0- Mindset Expanded/Redesigned-ConceptA"

    # Output PDF name
    output_pdf = os.path.join(base_dir, "M0-Mindset-Module-STARTUP-STYLE.pdf")

    # Collect all startup slides (01-57)
    slide_files = []
    for i in range(1, 58):
        slide_path = os.path.join(base_dir, f"slide-{i:02d}-startup.png")
        if os.path.exists(slide_path):
            slide_files.append(slide_path)
        else:
            print(f"⚠️  Warning: Missing slide-{i:02d}-startup.png")

    if not slide_files:
        print("❌ Error: No startup slide files found!")
        return

    print(f"📄 Compiling {len(slide_files)} slides to PDF...")
    print(f"📁 Output: {output_pdf}")
    print()

    # Open all images
    images = []
    for i, slide_path in enumerate(slide_files, 1):
        try:
            img = Image.open(slide_path)
            # Convert to RGB if needed (PDFs require RGB)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
            print(f"   ✓ Loaded slide {i:02d}")
        except Exception as e:
            print(f"   ❌ Error loading slide {i:02d}: {e}")

    if not images:
        print("❌ Error: No images loaded!")
        return

    # Save as PDF
    try:
        first_image = images[0]
        remaining_images = images[1:]

        first_image.save(
            output_pdf,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=remaining_images,
            optimize=True
        )

        print()
        print(f"✅ PDF compiled successfully!")
        print(f"📊 Total slides: {len(images)}")
        print(f"💾 Output: {output_pdf}")
        print()
        print("🎨 This PDF contains all slides with:")
        print("   • Startup presentation aesthetic")
        print("   • Dual-theme approach (light + dark)")
        print("   • Rounded card components")
        print("   • Soft gradient overlays")
        print("   • Numbered circular badges")
        print("   • Professional 2025 pitch deck design")

    except Exception as e:
        print(f"❌ Error creating PDF: {e}")

if __name__ == "__main__":
    compile_startup_slides_to_pdf()
