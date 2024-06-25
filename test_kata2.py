from kata2 import add
from pytest import raises

def testAddZero():
    assert add("") == 0

def testAddOne():
    assert add("1") == 1

def testAddTwo():
    assert add("1,2") == 3

def testAddThree():
    assert add("1,2,3") == 6
    assert add("1,2\n3") == 6

def testAddBadSeparation():
    with raises(ValueError):
        add("2,\n3")

def testAddNoTail():
    with raises(ValueError):
        add("1,2,")

def testAddCustomDelimiter():
    assert add("//;\n1;3") == 4
    assert add("//|\n1|2|3") == 6
    assert add("//sep\n2sep5") == 7

def testAddCustomException():
    with raises(ValueError) as exception:
        add("//|\n1|2,3")
        print(exception.value)
    assert str(exception.value) == "'|' expected but ',' found at position 3."