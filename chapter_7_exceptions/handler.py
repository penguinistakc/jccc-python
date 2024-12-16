#!/usr/bin/env python3
total = 9
while True:
    value = input("Please enter a number: ")
    if value == "end":
        break
    try:
        total += int(value)
    except ValueError:
        print("Invalid number - try again")

print("total is: ", total)
