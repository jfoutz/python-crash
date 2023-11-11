#!/usr/bin/env python3
from typing import List


def ch2_1() -> int:
    message: str = "Hello"
    return message


def ch2_2() -> str:
    """assign a var, print it, assign again and print again. hmm.
       we're just goint to assign twice."""
    message = "forgotton"
    message = "New Hello"
    return message


def ch2_3(name: str) -> str:
    return f"Hello {name}"


def ch2_4(name: str) -> List[str]:
    names = []
    names.append(name.title())
    names.append(name.lower())
    names.append(name.upper())
    return names


def ch2_5() -> str:
    who: str = "michael scott"
    quote: str = f"something famous -- {who.title()}"
    return quote


def ch2_6(person: str, quote: str) -> str:
    return f"'{person}' said '{quote}'"


def ch2_7a(name: str) -> str:
    return name.lstrip()


def ch2_7b(name: str) -> str:
    return name.rstrip()


def ch2_7c(name: str) -> str:
    return name.strip()


def ch2_8(name: str, suffix: str) -> str:
    return name.removesuffix(suffix)


def ch2_9() -> List[int]:
    vals: List[int] = []
    vals.append(2*4)
    vals.append(4+4)
    vals.append(16/2)
    return vals


def ch2_10() -> str:
    num: int = 42
    return f"My favorite number is {num}"
