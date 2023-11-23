#!/usr/bin/env python3
import chapters.ch5 as ch5


def test_ex1a() -> None:
    r = ch5.ex1()
    assert r[0:5] == [True, True, True, True, True]


def test_ex1b() -> None:
    r = ch5.ex1()
    assert r[5:] == [False, False, False, False, False]


def test_ex2a() -> None:
    r = ch5.ex2()
    assert r[0:5] == [True, True, True, True, True]


def test_ex2b() -> None:
    r = ch5.ex2()
    assert r[5:] == [False, False, False, False, False]


def test_ex3() -> None:
    assert ch5.ex3('green') == 5


def test_ex4a() -> None:
    assert ch5.ex4('green') == 5


def test_ex4b() -> None:
    assert ch5.ex4('blue') == 10


def test_ex5a() -> None:
    assert ch5.ex5('green') == 5


def test_ex5b() -> None:
    assert ch5.ex5('yellow') == 10


def test_ex5c() -> None:
    assert ch5.ex5('red') == 15


def test_ex6a() -> None:
    assert ch5.ex6(1) == 'baby'


def test_ex6b() -> None:
    assert ch5.ex6(3) == 'toddler'


def test_ex6c() -> None:
    assert ch5.ex6(10) == 'kid'


def test_ex6d() -> None:
    assert ch5.ex6(15) == 'teenager'


def test_ex6e() -> None:
    assert ch5.ex6(45) == 'adult'


def test_ex6f() -> None:
    assert ch5.ex6(75) == 'elder'
