#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run TTS, mux audio/video, and generate cover",
    )
    parser.add_argument("--video", default="manim.mp4")
    parser.add_argument("--output", default="output.mp4")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--log-file", help="Write command list to a file")
    parser.add_argument("--append-log", action="store_true")

    parser.add_argument("--tts-text")
    parser.add_argument("--tts-file")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural")
    parser.add_argument("--rate", default="+0%")
    parser.add_argument("--volume", default="+0%")

    parser.add_argument("--audio", help="Use an existing audio file")
    parser.add_argument("--audio-list", nargs="*", help="Concat audio list")
    parser.add_argument("--subs", help="Use an existing subtitle file (SRT)")
    parser.add_argument("--subs-output", help="Write subtitles when running TTS")

    parser.add_argument("--cover-title")
    parser.add_argument("--cover-subtitle", default="")
    parser.add_argument("--cover-output", default="cover.png")
    parser.add_argument("--cover-font")

    return parser.parse_args()


def run(
    cmd: list[str],
    dry_run: bool,
    verbose: bool,
    log_file: str | None,
    append_log: bool,
) -> None:
    if log_file:
        mode = "a" if append_log else "w"
        with open(log_file, mode, encoding="utf-8") as f:
            f.write(" ".join(cmd) + "\n")
    if verbose or dry_run:
        print(" ".join(cmd))
    if dry_run:
        return
    subprocess.run(cmd, check=True)


def main() -> None:
    args = parse_args()

    audio_path = args.audio
    subs_path = args.subs

    if not audio_path and args.audio_list:
        audio_path = "voice.mp3"
        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "concat_audio.py"),
            "--output",
            audio_path,
        ] + args.audio_list
        run(cmd, args.dry_run, args.verbose, args.log_file, args.append_log)

    if not audio_path and (args.tts_text or args.tts_file):
        audio_path = "voice.mp3"
        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "tts_generate.py"),
            "--voice",
            args.voice,
            "--rate",
            args.rate,
            "--volume",
            args.volume,
            "--output",
            audio_path,
        ]
        if args.subs_output:
            cmd += ["--subs-output", args.subs_output]
            subs_path = args.subs_output
        if args.tts_text:
            cmd += ["--text", args.tts_text]
        else:
            cmd += ["--text-file", args.tts_file]
        run(cmd, args.dry_run, args.verbose, args.log_file, args.append_log)

    if audio_path:
        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "mux_av.py"),
            "--video",
            args.video,
            "--audio",
            audio_path,
            "--output",
            args.output,
        ]
        if subs_path:
            cmd += ["--subs", subs_path]
        run(cmd, args.dry_run, args.verbose, args.log_file, args.append_log)

    if args.cover_title:
        cmd = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), "make_cover.py"),
            "--title",
            args.cover_title,
            "--subtitle",
            args.cover_subtitle,
            "--output",
            args.cover_output,
        ]
        if args.cover_font:
            cmd += ["--font", args.cover_font]
        run(cmd, args.dry_run, args.verbose, args.log_file, args.append_log)


if __name__ == "__main__":
    main()
