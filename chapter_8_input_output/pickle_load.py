#!/usr/bin/env python3

import pickle

f = open("output", "rb")

try:
    while True:
        obj = pickle.load(f)
        print(obj)
except EOFError:
    pass  # quietly ignoring since this is expected

f.close()
