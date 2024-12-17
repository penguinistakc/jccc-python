#!/usr/bin/env python3

import platform

data = ["mike", "jane", "alice", "ruth"]

p = platform.popen("sort", "r")
data = p.readlines()

for i in data:
    print(i, end="")

p.close()
