#!/usr/bin/env python3
import argparse
import os
import subprocess
import tempfile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Concatenate audio files with ffmpeg concat demuxer",
    )
    parser.add_argument("--inputs", nargs="*", help="List of audio files")
    parser.add_argument("--list-file", help="Path to a concat list file")
    parser.add_argument("--output", default="voice.mp3")
    return parser.parse_args()


def build_list_file(paths: list[str]) -> str:
    tmp = tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8")
    for p in paths:
        tmp.write(f"file '{os.path.abspath(p)}'\n")
    tmp.close()
    return tmp.name


def main() -> None:
    args = parse_args()
    list_file = args.list_file
    temp_created = False

    if not list_file:
        if not args.inputs:
            raise SystemExit("Provide --list-file or --inputs")
        list_file = build_list_file(args.inputs)
        temp_created = True

    cmd = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        list_file,
        "-c",
        "copy",
        args.output,
    ]
    subprocess.run(cmd, check=True)

    if temp_created:
        os.unlink(list_file)


if __name__ == "__main__":
    main()
