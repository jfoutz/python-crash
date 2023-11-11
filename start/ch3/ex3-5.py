#!/usr/bin/env python3

names = ['grandpa buddy']
names.append('grandpa bob')
names.append('mark twain')
names.append('mom')

cant = names.pop(2)

print(f"I'd like to have dinner with {names[0].title()}.")
print(f"I'd like to have dinner with {names[1].title()}.")
print(f"I'd like to have dinner with {names[2].title()}.")

print(f"{cant.title()} can't make it.")
