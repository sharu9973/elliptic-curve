from EC.EllipticCurve import EllipticCurve
from EC.Fp import Fp
from EC.PointOverEC import PointOverEC

import pytest


class TestPoint1:
    # y^2 = x^3 + 0x + b
    prime = 7
    a = Fp(0, prime)
    b = Fp(1, prime)
    curve = EllipticCurve(prime, a, b)

    def test_singlar(self):
        assert not self.curve.is_singular()

    def test_1(self):
        # 点どうしの演算テスト
        # p = (0, 1)
        p = PointOverEC(self.curve, Fp(0, self.prime), Fp(1, self.prime))
        assert p.is_valid()
        assert p + p == PointOverEC(self.curve, Fp(0, self.prime), Fp(6, self.prime))
        assert 2 * p == p + p
        assert p * 2 == p + p
        assert 10 * p == p + p + p + p + p + p + p + p + p + p

        # q = (2, 3)
        q = PointOverEC(self.curve, Fp(2, self.prime), Fp(3, self.prime))
        assert q.is_valid()
        # (0, 1) + (2, 3) = (6, 0)
        assert p + q == PointOverEC(self.curve, Fp(6, self.prime), Fp(0, self.prime))
        assert p + q == q + p

    def test_2(self):
        p = PointOverEC(self.curve, Fp(0, self.prime), Fp(1, self.prime))
        with pytest.raises(
            TypeError,
            match="Only scalar multiplication is defined. Do you mean pointwise addition?",
        ) as e:
            a = p * p

    def test_3(self):
        p = PointOverEC(self.curve, Fp(4, self.prime), Fp(4, self.prime))
        assert p.is_valid()
        p.print_subgroup()
