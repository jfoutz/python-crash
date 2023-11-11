#!/usr/bin/env python3
from typing import List


def ch2_1() -> int:
    message: str = "Hello"
    return message


def test_ch2_1() -> None:
    """get a message"""
    assert ch2_1() == 'Hello'


def ch2_2() -> str:
    """assign a var, print it, assign again and print again. hmm.
       we're just goint to assign twice."""
    message = "forgotton"
    message = "New Hello"
    return message


def test_ch2_2() -> None:
    assert ch2_2() == "New Hello"


def ch2_3(name: str) -> str:
    return f"Hello {name}"


def test_ch2_3() -> None:
    assert ch2_3('jason') == "Hello jason"


def ch2_4(name: str) -> List[str]:
    names = []
    names.append(name.title())
    names.append(name.lower())
    names.append(name.upper())
    return names


def test_ch2_4() -> None:
    assert ch2_4('jason') == ['Jason', 'jason', 'JASON']
