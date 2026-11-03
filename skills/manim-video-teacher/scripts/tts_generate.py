#!/usr/bin/env python3
import argparse
import asyncio
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate speech audio from text using edge-tts",
    )
    parser.add_argument("--text", help="Inline narration text")
    parser.add_argument("--text-file", help="Path to a UTF-8 text file")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural")
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--volume", default="+0%")
    parser.add_argument("--output", default="voice.mp3")
    parser.add_argument("--subs-output", help="Write subtitles to an SRT file")
    return parser.parse_args()


async def run_tts(
    text: str,
    voice: str,
    rate: str,
    volume: str,
    output: str,
    subs_output: str | None,
) -> None:
    try:
        import edge_tts
    except ImportError:
        print("edge-tts not installed. Run: pip install edge-tts", file=sys.stderr)
        raise SystemExit(1)

    communicate = edge_tts.Communicate(
        text,
        voice=voice,
        rate=rate,
        volume=volume,
        boundary="SentenceBoundary",
    )
    if not subs_output:
        await communicate.save(output)
        return

    submaker = edge_tts.SubMaker()
    with open(output, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)
    if hasattr(submaker, "generate_subs"):
        subs = submaker.generate_subs()
    elif hasattr(submaker, "get_srt"):
        subs = submaker.get_srt()
    else:
        raise RuntimeError("edge-tts SubMaker has no subtitle export method")
    with open(subs_output, "w", encoding="utf-8") as f:
        f.write(subs)


def load_text(args: argparse.Namespace) -> str:
    if args.text:
        return args.text
    if args.text_file:
        with open(args.text_file, "r", encoding="utf-8") as f:
            return f.read()
    print("Provide --text or --text-file", file=sys.stderr)
    raise SystemExit(2)


def main() -> None:
    args = parse_args()
    text = load_text(args)
    asyncio.run(
        run_tts(
            text,
            args.voice,
            args.rate,
            args.volume,
            args.output,
            args.subs_output,
        )
    )


if __name__ == "__main__":
    main()
