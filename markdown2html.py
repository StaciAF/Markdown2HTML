#!/usr/bin/python3
import sys

if __name__ == "__main__":
    while len(sys.argv) is 2:
        with open(sys.argv[1]) as md:
            if not md:
                print("Missing" + sys.argv[1])
                exit(1)
            else:
                exit()
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
