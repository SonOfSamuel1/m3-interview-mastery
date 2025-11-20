#!/usr/bin/env python3
"""
Compile ALL 42 M2- Reverse Attraction slides into a single PDF
"""

from PIL import Image
import os

print("\n" + "="*80)
print("COMPILING COMPLETE M2- REVERSE ATTRACTION MODULE INTO PDF")
print("All 42 Slides")
print("="*80 + "\n")

# Get all slide PNGs in order (1-42)
slides = []
for i in range(1, 43):
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
output_filename = "M2-Reverse-Attraction-COMPLETE.pdf"
images[0].save(
    output_filename,
    save_all=True,
    append_images=images[1:],
    resolution=72.0,
    quality=95
)

file_size = os.path.getsize(output_filename) / 1024 / 1024

print(f"\n✓ PDF created: {output_filename}")
print(f"  Pages: {len(images)}")
print(f"  Size: {file_size:.2f} MB")
print("\n" + "="*80)
print("MODULE COMPLETE!")
print("="*80)
print("\nModule Structure:")
print("  Slides 1-2: Title & Overview")
print("  Slides 3-7: Profile Foundation (Resume, Cover Letter, LinkedIn)")
print("  Slides 8-14: LinkedIn Sales Navigator & List Building")
print("  Slides 15-23: The Habit v.1 (LinkedIn Method)")
print("  Slides 24-36: The Habit v.2 (Email Method)")
print("  Slides 37-42: Module Summary & Next Steps")
print("\nTotal: 42 professional slides in Enhanced-WithGraphics style")
print("="*80 + "\n")
