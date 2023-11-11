#!/usr/bin/env python3

threes = []
for i in range(3, 30, 3):
    threes.append(i)
print(threes)

threes_prime = [x*3 for x in range(1, 10)]
print(threes_prime)
