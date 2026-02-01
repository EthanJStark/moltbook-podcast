#!/usr/bin/env python3
"""
Composite original lobster emoji with new larger text.
Takes the emoji region from original artwork and adds new text.
"""

from PIL import Image, ImageDraw, ImageFont

def create_gradient(width, height):
    """Create vertical blue gradient"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    top_color = (50, 80, 150)
    mid_color = (80, 128, 200)
    bottom_color = (124, 170, 230)

    for y in range(height):
        if y < height / 2:
            ratio = y / (height / 2)
            r = int(top_color[0] + (mid_color[0] - top_color[0]) * ratio)
            g = int(top_color[1] + (mid_color[1] - top_color[1]) * ratio)
            b = int(top_color[2] + (mid_color[2] - top_color[2]) * ratio)
        else:
            ratio = (y - height / 2) / (height / 2)
            r = int(mid_color[0] + (bottom_color[0] - mid_color[0]) * ratio)
            g = int(mid_color[1] + (bottom_color[1] - mid_color[1]) * ratio)
            b = int(mid_color[2] + (bottom_color[2] - mid_color[2]) * ratio)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

def main():
    width = 3000
    height = 3000

    # Create new background
    print("Creating gradient background...")
    img = create_gradient(width, height)

    # Load original artwork to extract lobster
    print("Extracting lobster emoji from original artwork...")
    try:
        original = Image.open("artwork.jpg")
        # Extract lobster region (roughly centered, top portion)
        # Original has lobster at around y=1400, size ~1200px
        # Extract generously to get the whole emoji
        lobster_region = original.crop((600, 200, 2400, 1600))

        # Paste onto new background
        img.paste(lobster_region, (600, 200))
        print("✓ Lobster emoji extracted and placed")
    except Exception as e:
        print(f"Warning: Could not extract lobster from original: {e}")
        print("Continuing with just text...")

    # Add new larger text
    print("Adding title text...")
    draw = ImageDraw.Draw(img)

    try:
        text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 280)
    except:
        try:
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 280)
        except:
            print("Warning: Could not load font, using default")
            text_font = ImageFont.load_default()

    title_text = "The Moltbook Report"
    bbox = draw.textbbox((0, 0), title_text, font=text_font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    text_y = 2150

    # Add text with slight shadow for better readability
    # Shadow
    draw.text((text_x + 4, text_y + 4), title_text, font=text_font, fill=(0, 0, 0, 128))
    # Main text
    draw.text((text_x, text_y), title_text, font=text_font, fill=(255, 255, 255))

    # Save
    output_path = "artwork-v2.jpg"
    print(f"Saving to {output_path}...")
    img.save(output_path, "JPEG", quality=95, optimize=True)
    print(f"✓ Artwork generated: {output_path}")
    print(f"  Size: {width}x{height}px")
    print(f"  Text: {title_text} (280px font)")

if __name__ == "__main__":
    main()
