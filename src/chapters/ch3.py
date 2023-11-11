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
