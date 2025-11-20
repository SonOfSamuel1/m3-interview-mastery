#!/usr/bin/env python3
"""
Compile all M1-Profile Matching slides into final comprehensive PDF
Including all enhancements: new slides, case studies, and updated content
"""

from PIL import Image
import os
import glob

def compile_final_pdf():
    """Compile all slides in proper order"""

    slides_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching"

    print("Compiling M1-Profile Matching Module - Enhanced Edition")
    print("=" * 60)

    # Define slide order
    slide_order = [
        # Original slides 1-18
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        # New compensation breakdowns
        '18A', '18B', '18C',
        # Continue with original slides
        '19', '20', '21', '22', '23', '24', '25', '26', '27',
        # Original career development slides
        '28', '29', '30', '31', '32',
        # Case studies
        'CS1-1', 'CS1-2', 'CS2-1', 'CS2-2', 'CS3-1', 'CS3-2'
    ]

    # Load all images
    images = []
    missing_slides = []

    for slide_num in slide_order:
        img_path = os.path.join(slides_dir, f"{slide_num}.png")
        if os.path.exists(img_path):
            img = Image.open(img_path)
            # Convert to RGB if necessary (PDFs don't support RGBA)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
            print(f"  ✓ Loaded slide {slide_num}")
        else:
            missing_slides.append(slide_num)
            print(f"  ⚠ Missing slide {slide_num}")

    if missing_slides:
        print(f"\nWarning: {len(missing_slides)} slides missing: {', '.join(missing_slides)}")
        print("Continuing with available slides...")

    # Output PDF path
    output_pdf = os.path.join(slides_dir, "M1-Profile-Matching-ENHANCED-COMPLETE.pdf")

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
        print(f"\n{'='*60}")
        print(f"✓ ENHANCED PDF CREATED SUCCESSFULLY!")
        print(f"  Location: {output_pdf}")
        print(f"  Total slides: {len(images)}")
        print(f"  Original module: 32 slides")
        print(f"  New content: {len(images) - 32} slides")
        print("="*60)
        print("\nENHANCEMENTS SUMMARY:")
        print("  • Updated Slide 11 (new terminology)")
        print("  • Updated Slide 20 (self-assessment framework)")
        print("  • Updated Slides 25-27 (company examples)")
        print("  • Updated Slides 28-32 (career development paths)")
        print("  • New Slides 18A-C (profile-specific compensation)")
        print("  • New Case Study Slides (6 slides, 3 case studies)")
        print("\nDOWNLOADABLE RESOURCES CREATED:")
        print("  • Company Evaluation Scorecard (Excel)")
        print("  • Target Company List Template (Excel, 50+ companies)")
        print("  • Self-Assessment Worksheet (PDF)")
        print("="*60)
        return output_pdf
    else:
        print("Error: No images found to compile")
        return None

def main():
    compile_final_pdf()

if __name__ == "__main__":
    main()
