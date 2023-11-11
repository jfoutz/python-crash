#!/usr/bin/env python3
from chapters.ch2 import ch2_1, ch2_2, ch2_3, ch2_4


def test_ch2_1() -> None:
    """get a message"""
    assert ch2_1() == 'Hello'


def test_ch2_2() -> None:
    assert ch2_2() == "New Hello"


def test_ch2_3() -> None:
    assert ch2_3('jason') == "Hello jason"


def test_ch2_4() -> None:
    assert ch2_4('jason') == ['Jason', 'jason', 'JASON']
