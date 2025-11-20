from PIL import Image
import os
import sys

# Get all PNG files and sort them numerically
png_files = [f for f in os.listdir('.') if f.endswith('.png') and f[:-4].isdigit()]
png_files.sort(key=lambda x: int(x[:-4]))

print(f'Found {len(png_files)} slides to process...')

# Open all images
images = []
for i, png_file in enumerate(png_files, 1):
    print(f'Processing slide {i}/{len(png_files)}: {png_file}')
    img = Image.open(png_file)
    # Convert to RGB if needed (PDF requires RGB)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    images.append(img)

# Save as PDF
if images:
    print('Creating PDF...')
    images[0].save('M0-Mindset-Module-Complete.pdf', save_all=True, append_images=images[1:], resolution=100.0)
    print(f'Successfully created: M0-Mindset-Module-Complete.pdf')
    print(f'Total slides: {len(images)}')
else:
    print('Error: No slides found')
    sys.exit(1)
