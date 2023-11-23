#!/usr/bin/env python3
from typing import List


def ex1() -> List[bool]:
    res: List[bool] = []
    res.append(2 + 2 == 4)
    res.append('audi' == 'Audi'.lower())
    res.append(3 < 5)
    res.append('hello'.islower())
    res.append(2**3 == 8)

    res.append(2 + 2 == 5)
    res.append('Audi' == 'Audi'.lower())
    res.append(3 > 5)
    res.append('hello'.isupper())
    res.append(2**3 != 8)
    return res


def ex2() -> List[bool]:
    res: List[bool] = []
    stuff: List[str] = ['foo', 'BAR', 'Baz']
    res.append('foo' == 'Foo'.lower())
    res.append(3 < 2 or 2 < 3)
    res.append('foo' in stuff)
    res.append(True and not False)
    res.append('BAR' in stuff)
    res.append('foo' == 'Foo')
    res.append(3 < 2 and 2 < 3)
    res.append('Bar' in stuff)
    res.append(False and not True)
    res.append('bar' in stuff)
    return res


def ex3(color: str) -> int:
    if color == 'green':
        return 5
    return None


def ex4(color: str) -> int:
    if color == 'green':
        return 5
    else:
        return 10


def ex5(color: str) -> int:
    if color == 'green':
        return 5
    elif color == 'yellow':
        return 10
    elif color == 'red':
        return 15
    return None


def ex6(age: int) -> str:
    if age < 2:
        return 'baby'
    elif age < 4:
        return 'toddler'
    elif age < 13:
        return 'kid'
    elif age < 20:
        return 'teenager'
    elif age < 65:
        return 'adult'
    else:
        return 'elder'
