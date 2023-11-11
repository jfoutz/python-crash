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


