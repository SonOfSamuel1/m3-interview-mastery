#!/usr/bin/env python3
"""
Compile all premium slide PNG files into a single PDF
"""

from PIL import Image
import os

def compile_premium_slides_to_pdf():
    """Compile all slide-XX-premium.png files into a single PDF"""

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all premium slide PNG files and sort them
    slide_files = [f for f in os.listdir(script_dir)
                   if f.startswith('slide-') and f.endswith('-premium.png')]
    slide_files.sort()

    if not slide_files:
        print("No premium slide PNG files found!")
        return

    print(f"Found {len(slide_files)} premium slides to compile...")

    # Load all images
    images = []
    for slide_file in slide_files:
        file_path = os.path.join(script_dir, slide_file)
        img = Image.open(file_path)
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            images.append(rgb_img)
        else:
            images.append(img.convert('RGB'))
        print(f"  Loaded {slide_file}")

    # Save as PDF
    output_path = os.path.join(script_dir, "M0-Mindset-Module-PREMIUM.pdf")

    if images:
        # First image is the base, rest are appended
        images[0].save(
            output_path,
            save_all=True,
            append_images=images[1:],
            resolution=100.0,
            quality=95
        )
        print(f"\n✓ Successfully created premium PDF: {output_path}")
        print(f"  Total pages: {len(images)}")
        print(f"  Quality: High-resolution (95% quality)")
        print(f"  Ready for $5,000 course delivery!")
    else:
        print("No images to compile!")

if __name__ == "__main__":
    compile_premium_slides_to_pdf()
