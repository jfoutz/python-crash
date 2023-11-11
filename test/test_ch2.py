#!/usr/bin/env python3
import chapters.ch2 as chapter


def test_ch2_1() -> None:
    """get a message"""
    assert chapter.ch2_1() == 'Hello'


def test_ch2_2() -> None:
    assert chapter.ch2_2() == "New Hello"


def test_ch2_3() -> None:
    assert chapter.ch2_3('jason') == "Hello jason"


def test_ch2_4() -> None:
    assert chapter.ch2_4('jason') == ['Jason', 'jason', 'JASON']


def test_ch2_5() -> None:
    assert chapter.ch2_5() == "something famous -- Michael Scott"


def test_ch2_6() -> None:
    res: str = "'jason' said 'testing is weird'"
    assert chapter.ch2_6("jason", "testing is weird") == res


def test_ch2_7a() -> None:
    assert chapter.ch2_7a('\tjason\n') == 'jason\n'


def test_ch2_7b() -> None:
    assert chapter.ch2_7b('\tjason\n') == '\tjason'


def test_ch2_7c() -> None:
    assert chapter.ch2_7c('\tjason\n') == 'jason'


def test_ch2_8() -> None:
    assert chapter.ch2_8('myfile.txt', '.txt') == 'myfile'


def test_ch2_9() -> None:
    assert chapter.ch2_9() == [8, 8, 8]


def test_ch2_10() -> None:
    assert chapter.ch2_10() == 'My favorite number is 42'
