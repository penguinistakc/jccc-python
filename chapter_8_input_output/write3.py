#!/usr/in/env python3

filename = input("Enter a filename: ")
f = open(filename, "w")
f.write("This is a test\n")
f.write("This is another test\n")
f.close()
