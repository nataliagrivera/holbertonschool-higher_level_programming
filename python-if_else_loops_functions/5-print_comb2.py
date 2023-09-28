#!/usr/bin/python3
output = ""
for i in range(100):
    output += f"{i:02d}, " if i < 99 else f"{i:02d}\n"

print(output, end="")
