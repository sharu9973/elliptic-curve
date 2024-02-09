from EC.Fp import Fp
from EC.Fp2 import Fp2


def test_1():
    # p % 4 == 3
    p = 7
    a = Fp(0, p)
    b = Fp(0, p)
    x = Fp2(a, b)
    assert x.ch == p
    assert x.order == p**2
    assert x.beta_sq == Fp(6, p)


def test_2():
    # p % 4 == 1
    p = 5
    a = Fp(0, p)
    b = Fp(0, p)
    x = Fp2(a, b)
    assert x.ch == p
    assert x.order == p**2
    assert x.beta_sq == Fp(2, p)


def test_3():
    p = 5
    a = Fp(1, p)
    b = Fp(2, p)
    c = Fp(2, p)
    d = Fp(1, p)
    x = Fp2(a, b)
    y = Fp2(c, d)
    assert x.beta_sq == Fp(2, p)
    assert x + y == Fp2(Fp(3, p), Fp(3, p))
    assert x * y == Fp2(Fp(1, p), Fp(0, p))
