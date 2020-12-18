#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    with open(sys.argv[1]) as md:
        if not md:
            print("Missing" + sys.argv[1])
            exit(1)
    exit()
