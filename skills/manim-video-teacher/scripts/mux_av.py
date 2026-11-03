#!/usr/bin/env python3
import argparse
import subprocess


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mux video and audio into a single MP4 using ffmpeg",
    )
    parser.add_argument("--video", required=True)
    parser.add_argument("--audio", required=True)
    parser.add_argument("--subs", help="Optional SRT subtitles to embed")
    parser.add_argument("--output", default="output.mp4")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cmd = [
        "ffmpeg",
        "-i",
        args.video,
        "-i",
        args.audio,
    ]
    if args.subs:
        cmd += [
            "-i",
            args.subs,
            "-c:s",
            "mov_text",
            "-metadata:s:s:0",
            "language=chi",
        ]
    cmd += [
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        args.output,
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
