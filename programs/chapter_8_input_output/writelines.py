#!/usr/bin/env python3

f = open("output", "w")
lis = []

while True:
    data = input("Enter data ('q' to quit): ")
    if data == "q":
        break
    lis.append(data)

f.writelines(lis)
f.close()
