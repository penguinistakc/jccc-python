#!/usr/bin/env python3

f = open("output", "w")

while True:
    data = input("Enter data ('q' to quit): ")
    if data == "q":
        break
    print(data, file=f)

f.close()
