#!/usr/bin/env python3
import argparse

from headtailx.headtailx_common import HeadTail


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Output the last part of files."
    )
    parser.add_argument("file", type=str, help="File path")
    parser.add_argument(
        "-n", "--lines", type=int, default=10, help="Number of lines (default: 10)"
    )
    parser.add_argument("-c", "--bytes", type=int, default=None, help="Number of bytes")
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Never print headers giving file names",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Always print headers giving file names",
    )
    parser.add_argument(
        "-z",
        "--zero-terminated",
        action="store_true",
        help="Line delimiter is NUL, not newline",
    )

    args: argparse.Namespace = parser.parse_args()

    head_tail = HeadTail(
        file_path=args.file,
        num_lines=args.lines,
        num_bytes=args.bytes,
        quiet=args.quiet,
        verbose=args.verbose,
        zero_terminated=args.zero_terminated,
    )

    print(head_tail.tail())


if __name__ == "__main__":
    main()
