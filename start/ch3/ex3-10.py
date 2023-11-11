#!/usr/bin/env python3

stuff = ['java', 'golang', 'python', 'haskell', 'agda']

print(f"len:        {len(stuff)}")
print(f"plain:      {stuff}")
print(f"sorted:     {sorted(stuff)}")
print(f"rev:        {sorted(stuff, reverse=True)}")
print(f"plain:      {stuff}")
stuff.sort()
print(f"mutate sort:{stuff}")
stuff.sort(reverse=True)
print(f"mutate rev: {stuff}")
