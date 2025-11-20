#!/usr/bin/env python3
"""
Compile all M1-Profile Matching slides into a single PDF
"""

from PIL import Image
import os

def compile_slides_to_pdf():
    """Compile all PNG slides in M1 directory into a single PDF"""

    # Directory containing the slides
    slides_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching"

    # Get all PNG files and sort them numerically
    png_files = [f for f in os.listdir(slides_dir) if f.endswith('.png')]
    png_files.sort(key=lambda x: int(x.replace('.png', '')))

    print(f"Found {len(png_files)} slides to compile...")

    # Load all images
    images = []
    for png_file in png_files:
        img_path = os.path.join(slides_dir, png_file)
        img = Image.open(img_path)
        # Convert to RGB if necessary (PDFs don't support RGBA)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)
        print(f"  ✓ Loaded {png_file}")

    # Output PDF path
    output_pdf = os.path.join(slides_dir, "M1-Profile-Matching-Complete.pdf")

    # Save as PDF
    if images:
        # First image is the base, rest are appended
        images[0].save(
            output_pdf,
            save_all=True,
            append_images=images[1:],
            resolution=100.0,
            quality=95
        )
        print(f"\n✓ PDF created successfully!")
        print(f"  Location: {output_pdf}")
        print(f"  Total slides: {len(images)}")
        return output_pdf
    else:
        print("Error: No images found to compile")
        return None

if __name__ == "__main__":
    compile_slides_to_pdf()
