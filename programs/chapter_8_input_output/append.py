#!/usr/in/env python3

f = open("test.txt", "a")
f.write("Appended to the bottom\n")
f.write(" of the file\n")
f.write("More at the bottom\n")
f.close()
