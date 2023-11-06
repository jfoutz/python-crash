#!/usr/bin/env python3
message = "Hello python world!"

print(message)

name = "ada lovelace"
print(name.title())

name2 = "Ada Lovelace"
print(name2.upper())
print(name2.lower())

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)

greet = f"Hello, {full_name.title()}"
print(greet)
# p22, newlines

print("Languages:\n\tPython\n\tC\n\tJavaScript")


stripex = '  python  '
print(stripex.rstrip())
print(stripex.lstrip())
print(stripex.strip())

nostarch_url = "https://nostarch.com"
nostarch_short = nostarch_url.removeprefix('https://')
print(nostarch_url)
print(nostarch_short)
