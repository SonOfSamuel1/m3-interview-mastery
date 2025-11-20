#!/usr/bin/env python3
"""
Compile all M2- Reverse Attraction slides into a single PDF
"""

from PIL import Image
import os

print("\n" + "="*80)
print("COMPILING M2- REVERSE ATTRACTION SLIDES INTO PDF")
print("="*80 + "\n")

# Get all slide PNGs in order
slides = []
for i in range(1, 25):
    filename = f"{i}.png"
    if os.path.exists(filename):
        print(f"Adding Slide {i}... {filename}")
        slides.append(filename)
    else:
        print(f"⚠ Warning: {filename} not found")

if not slides:
    print("✗ No slides found!")
    exit(1)

print(f"\nTotal slides found: {len(slides)}")
print("Converting to PDF...")

# Open all images
images = [Image.open(slide).convert('RGB') for slide in slides]

# Save as PDF
output_filename = "M2-Reverse-Attraction-Complete.pdf"
images[0].save(
    output_filename,
    save_all=True,
    append_images=images[1:],
    resolution=72.0,
    quality=95
)

print(f"\n✓ PDF created: {output_filename}")
print(f"  Pages: {len(images)}")
print(f"  Size: {os.path.getsize(output_filename) / 1024 / 1024:.2f} MB")
print("="*80 + "\n")
