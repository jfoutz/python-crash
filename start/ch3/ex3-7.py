#!/usr/bin/env python3

names = ['grandpa buddy']
names.append('grandpa bob')
names.append('mark twain')
names.append('mom')
names.insert(3, 'dad')
names.insert(1, 'grandma sally')

print("the dinner table is to small!")
cant = names.pop(2)
print(f"i'm sorry {cant.title()} there's no room at the table.")
cant = names.pop(0)
print(f"i'm sorry {cant.title()} there's no room at the table.")
cant = names.pop(0)
print(f"i'm sorry {cant.title()} there's no room at the table.")
cant = names.pop(0)
print(f"i'm sorry {cant.title()} there's no room at the table.")

print(f"I'd like to invite {names[0].title()} to dinner.")
print(f"I'd like to invite {names[1].title()} to dinner.")
