#!/usr/bin/env python3
from typing import List


def ex1() -> str:
    names: List[str] = ['a', 'b', 'c']
    res: str = names[0] + names[1] + names[2]
    return res


def ex2() -> str:
    names: List[str] = ['a', 'b', 'c']
    res: str = ""
    for name in names:
        res += f"hello {name}\n"
    return res


def ex3() -> str:
    stuff: List[str] = ['a', 'b', 'c']
    res: str = ""
    for item in stuff:
        res += f"want {item}\n"
    return res


def ex4() -> str:
    people: List[str] = ['bob smith', 'sam jones', 'joe dirt']
    msg: str = ""
    for person in people:
        msg += f"Hi {person.title()}, please come to dinner\n"
    return msg


def ex5() -> str:
    people: List[str] = ['bob smith', 'sam jones', 'joe dirt']
    unavailable: str = people.pop(0)
    people.append('mom')
    msg: str = f"{unavailable.title()} can't make it.\n"
    for person in people:
        msg += f"Hi {person.title()}, please come to dinner\n"
    return msg


def ex6() -> str:
    people: List[str] = ['bob smith', 'sam jones', 'joe dirt']
    people.insert(0, 'mom')
    people.insert(2, 'dad')
    people.append('other')
    msg: str = "We got a bigger table.\n"
    for person in people:
        msg += f"Hi {person.title()}, please come to dinner\n"
    return msg


def ex7() -> str:
    people: List[str] = ['bob smith', 'sam jones', 'joe dirt']
    people.insert(0, 'mom')
    people.insert(2, 'dad')
    people.append('other')
    msg: str = "We can only invite 2 people.\n"
    nix: str = ""
    for i in range(0, 4):
        nix = people.pop()
        msg += f"Sorry {nix.title()} we don't have space.\n"

    for person in people:
        msg += f"Hi {person.title()}, please come to dinner\n"

    del people[0]
    del people[0]
    msg += f"{people}\n"
    return msg


def ex8(places: List[str]) -> str:
    res: str = "["
    for i in places:
        res += f"{i} "
    res += "]\n["
    for i in sorted(places):
        res += f"{i} "
    res += "]\n["
    for i in places:
        res += f"{i} "
    res += "]\n["
