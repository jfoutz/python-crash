#!/usr/bin/env python3
from typing import List, Tuple


def ex1() -> str:

    toppings: List[str] = ['olives', 'pepperoni', 'mushrooms']
    res: str = ""
    for top in toppings:
        res += f"i like {top}\n"
    res += "pizza is great\n"
    return res


def ex2() -> str:
    animals: List[str] = ['dog', 'cat', 'rat']

    res: str = ""
    for a in animals:
        res += f"{a}\n"

    for a in animals:
        res += f"a {a} would be a good pet\n"

    res += "these animals have 4 legs\n"
    return res


def ex3() -> List[int]:
    res: List[int] = []
    for i in range(1, 21):
        res.append(i)
    return res


def ex4() -> List[int]:
    res: List[int] = []
    for i in range(1, 1_000_001):
        res.append(i)
    return res


def ex5() -> Tuple[int, int, int]:
    ls: List[int] = range(1, 1_000_001)
    return (min(ls), max(ls), sum(ls))


def ex6() -> List[int]:
    return [x for x in range(1, 20, 2)]


def ex7() -> List[int]:
    return [x for x in range(3, 31, 3)]


def ex8() -> List[int]:
    return [x**3 for x in range(1, 11)]


# def ex9() -> List[int]:
# as above but use a comprehension, which... i did.


def ex10() -> Tuple[List[str], List[str], List[str]]:
    animals: List[str] = ['dog', 'cat', 'rat', 'bat', 'ant']
    res: Tuple[List[str], List[str], List[str]] = (
        animals[:3],
        animals[1:4],
        animals[2:]
    )
    return res


def ex11() -> Tuple[List[str], List[str], List[str]]:
    pizza: List[str] = ['pepperoni']
    mine: List[str] = pizza[:]
    mine.append('olive')
    theirs: List[str] = pizza[:]
    theirs.append('mushroom')
    return (pizza, mine, theirs)


def ex12() -> str:
    (f, m, e) = ex10()
    res = ""
    for item in f:
        res += f"{item}\t"
    res += '\n'
    for item in m:
        res += f"{item}\t"
    res += '\n'
    for item in e:
        res += f"{item}\t"
    res += '\n'
    return res


def ex13() -> str:
    foods = ('apple', 'orange', 'banana')
    res = ""
    for f in foods:
        res += f"{f}\n"
    #  change food fails
    #  foods[0] = 'candy'
    foods = ('candy', 'pie', 'cake')
    for f in foods:
        res += f"{f}\n"
    return res
