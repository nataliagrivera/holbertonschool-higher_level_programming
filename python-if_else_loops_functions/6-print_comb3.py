#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i < 8:
            print(f"{i:d}{j:d}, ", end="")
        else:
            print(f"{i:d}{j:d}\n", end="")
