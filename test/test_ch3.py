#!/usr/bin/env python3

import chapters.ch3 as ch3


def test_ex1() -> None:
    assert ch3.ex1() == 'abc'


def test_ex2() -> None:
    assert ch3.ex2() == 'hello a\nhello b\nhello c\n'


def test_ex3() -> None:
    assert ch3.ex3() == 'want a\nwant b\nwant c\n'


def test_ex4() -> None:
    assert ch3.ex4() == ('Hi Bob Smith, please come to dinner\n'
                         'Hi Sam Jones, please come to dinner\n'
                         'Hi Joe Dirt, please come to dinner\n')


def test_ex5() -> None:
    assert ch3.ex5() == ('Bob Smith can\'t make it.\n'
                         'Hi Sam Jones, please come to dinner\n'
                         'Hi Joe Dirt, please come to dinner\n'
                         'Hi Mom, please come to dinner\n')


def test_ex6() -> None:
    assert ch3.ex6() == ('We got a bigger table.\n'
                         'Hi Mom, please come to dinner\n'
                         'Hi Bob Smith, please come to dinner\n'
                         'Hi Dad, please come to dinner\n'
                         'Hi Sam Jones, please come to dinner\n'
                         'Hi Joe Dirt, please come to dinner\n'
                         'Hi Other, please come to dinner\n')


def test_ex7() -> None:
    assert ch3.ex7() == ("We can only invite 2 people.\n"
                         'Sorry Other we don\'t have space.\n'
                         'Sorry Joe Dirt we don\'t have space.\n'
                         'Sorry Sam Jones we don\'t have space.\n'
                         'Sorry Dad we don\'t have space.\n'
                         'Hi Mom, please come to dinner\n'
                         'Hi Bob Smith, please come to dinner\n'
                         '[]\n')
