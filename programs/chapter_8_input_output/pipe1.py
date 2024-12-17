#!/usr/bin/env python3

import subprocess


def list_files_in_dir(directory):
    p = subprocess.run(["ls", directory], capture_output=True, text=True)
    return p.stdout.splitlines()


if __name__ == "__main__":
    for i in list_files_in_dir("."):
        print(i)
