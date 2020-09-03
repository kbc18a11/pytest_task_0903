from functions import isPrime, calcDistance


def test_calcDistance3333():
    assert calcDistance(3, 3, 3, 3) == 0


def test_calcDistance3377():
    assert calcDistance(3, 3, 7, 7) == 5.656854249492381


def test_calcDistance22_1_1():
    assert calcDistance(2, 2, -1, -1) == 4.242640687119285


def test_calcDistance_2_2_5_5():
    assert calcDistance(-2, -2, -5, -5) == 4.242640687119285


def test_calcDistance0000():
    assert calcDistance(0, 0, 0, 0) == 0


def test_isPrime2():
    assert isPrime(2)


def test_isPrime3():
    assert isPrime(3)


def test_isPrime5():
    assert isPrime(5)


def test_isPrime7():
    assert isPrime(7)


def test_isPrime13():
    assert isPrime(13)
