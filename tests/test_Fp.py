from EC.Fp import Fp


def test_1():
    p = 7
    a = Fp(0, p)
    b = Fp(8, p)
    assert a + b == Fp(1, p)
    assert a * b == Fp(0, p)


def test_2():
    p = 11
    a = Fp(2, p)
    b = Fp(8, p)
    assert a + b == Fp(10, p)
    assert a * b == Fp(5, p)
    assert a / b == Fp(3, p)


def test_3():
    p = 11
    a = Fp(2, p)
    assert 3 * a == Fp(6, p)
    assert a * 4 == Fp(8, p)
