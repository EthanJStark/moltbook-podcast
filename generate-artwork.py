#!/usr/bin/env python3
"""
Generate podcast artwork with lobster emoji and larger text.

Requirements: pip install pillow

Usage: python3 generate-artwork.py

Generates: artwork-final.jpg (3000x3000px with gradient background,
lobster emoji, and "The Moltbook Report" text)
"""

from PIL import Image, ImageDraw, ImageFont
import sys

def create_gradient(width, height):
    """Create vertical blue gradient matching original artwork"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Gradient colors from original: #325096 -> #5080C8 -> #7CAAE6
    top_color = (50, 80, 150)      # #325096
    mid_color = (80, 128, 200)     # #5080C8
    bottom_color = (124, 170, 230) # #7CAAE6

    for y in range(height):
        if y < height / 2:
            # Top half: blend from top to mid
            ratio = y / (height / 2)
            r = int(top_color[0] + (mid_color[0] - top_color[0]) * ratio)
            g = int(top_color[1] + (mid_color[1] - top_color[1]) * ratio)
            b = int(top_color[2] + (mid_color[2] - top_color[2]) * ratio)
        else:
            # Bottom half: blend from mid to bottom
            ratio = (y - height / 2) / (height / 2)
            r = int(mid_color[0] + (bottom_color[0] - mid_color[0]) * ratio)
            g = int(mid_color[1] + (bottom_color[1] - mid_color[1]) * ratio)
            b = int(mid_color[2] + (bottom_color[2] - mid_color[2]) * ratio)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

def main():
    # Canvas settings
    width = 3000
    height = 3000

    # Create gradient background
    print("Creating gradient background...")
    img = create_gradient(width, height)
    draw = ImageDraw.Draw(img)

    # Add lobster emoji
    # Note: For emoji to render correctly, you need a font that supports color emoji
    # On macOS, use Apple Color Emoji font
    # On Linux, use Noto Color Emoji
    print("Adding lobster emoji...")
    try:
        # Try macOS font first
        emoji_font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 1200)
    except:
        try:
            # Try Linux font
            emoji_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 1200)
        except:
            print("Warning: Could not load emoji font. Emoji may not render correctly.")
            emoji_font = ImageFont.load_default()

    lobster_emoji = "🦞"
    bbox = draw.textbbox((0, 0), lobster_emoji, font=emoji_font)
    emoji_width = bbox[2] - bbox[0]
    emoji_x = (width - emoji_width) // 2
    emoji_y = 600  # Positioned higher to make room for text
    draw.text((emoji_x, emoji_y), lobster_emoji, font=emoji_font, embedded_color=True)

    # Add text
    print("Adding title text...")
    try:
        # Try to use a clean sans-serif font
        text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 280)
    except:
        try:
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 280)
        except:
            print("Warning: Could not load preferred font. Using default.")
            text_font = ImageFont.load_default()

    title_text = "The Moltbook Report"
    bbox = draw.textbbox((0, 0), title_text, font=text_font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    text_y = 2150  # Positioned below emoji

    draw.text((text_x, text_y), title_text, font=text_font, fill=(255, 255, 255))

    # Save
    output_path = "artwork-final.jpg"
    print(f"Saving to {output_path}...")
    img.save(output_path, "JPEG", quality=95)
    print(f"✓ Artwork generated successfully: {output_path}")
    print(f"  Size: {width}x{height}px")
    print(f"  Text: {title_text}")

    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except ImportError as e:
        print(f"Error: Missing required module: {e}")
        print("Install with: pip3 install pillow")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
