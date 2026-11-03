#!/usr/bin/env python3
import argparse
from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a simple 16:9 cover image",
    )
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--output", default="cover.png")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--bg", default="#0E1A2B")
    parser.add_argument("--accent", default="#FFB000")
    parser.add_argument("--font", help="Optional path to a .ttf font")
    return parser.parse_args()


def load_font(path: str | None, size: int) -> ImageFont.ImageFont:
    if path:
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main() -> None:
    args = parse_args()
    img = Image.new("RGB", (args.width, args.height), args.bg)
    draw = ImageDraw.Draw(img)

    title_font = load_font(args.font, 96)
    subtitle_font = load_font(args.font, 48)

    margin_x = int(args.width * 0.1)
    margin_y = int(args.height * 0.18)

    draw.text((margin_x, margin_y), args.title, font=title_font, fill="white")
    if args.subtitle:
        draw.text(
            (margin_x, margin_y + 130),
            args.subtitle,
            font=subtitle_font,
            fill=args.accent,
        )

    img.save(args.output)


if __name__ == "__main__":
    main()
