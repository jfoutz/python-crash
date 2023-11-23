#!/usr/bin/env python3
import chapters.ch4 as ch4


def test_ex1() -> None:
    assert ch4.ex1() == ('i like olives\ni like pepperoni\n'
                         'i like mushrooms\npizza is great\n'
                         )


def test_ex2() -> None:
    assert ch4.ex2() == ('dog\ncat\nrat\n'
                         'a dog would be a good pet\n'
                         'a cat would be a good pet\n'
                         'a rat would be a good pet\n'
                         'these animals have 4 legs\n'
                         )


def test_ex3() -> None:
    assert ch4.ex3() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                         , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def test_ex4() -> None:
    assert len(ch4.ex4()) == 1_000_000


def test_ex5() -> None:
    assert ch4.ex5() == (1, 1_000_000, 1_000_001 * 500_000)


def test_ex6() -> None:
    assert ch4.ex6() == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def test_ex7() -> None:
    assert ch4.ex7() == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


def test_ex8() -> None:
    assert ch4.ex8() == [1, 8, 27, 64, 125, 36*6, 7*7*7, 8*8*8, 9*9*9, 1000]

# ex9 skipped


def test_ex10() -> None:
    assert ch4.ex10() == (['dog', 'cat', 'rat'],
                         ['cat', 'rat', 'bat'],
                         ['rat', 'bat', 'ant'])


def test_ex11() -> None:
    assert ch4.ex11() == (['pepperoni'],
                          ['pepperoni', 'olive'],
                          ['pepperoni', 'mushroom'])


def test_ex12() -> None:
    assert ch4.ex12() == ('dog\tcat\trat\t\n'
                          'cat\trat\tbat\t\n'
                          'rat\tbat\tant\t\n')


def test_ex13() -> None:
    assert ch4.ex13() == ('apple\norange\nbanana\n'
                          'candy\npie\ncake\n')
