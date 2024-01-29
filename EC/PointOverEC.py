from .EllipticCurve import EllipticCurve
from .Fp import Fp

from typing import Self


class PointOverEC:
    def __init__(self, curve: EllipticCurve, x, y, is_point_at_infinity=False):
        self.curve = curve
        self.x = x
        self.y = y
        self.is_point_at_infinity = is_point_at_infinity

    def id(self):
        return self.__class__(self.curve, 0, 0, True)

    def is_valid(self) -> bool:
        """return whether (x, y) is a rational point on the curve."""
        return (
            self.y * self.y
            == self.x * self.x * self.x + self.curve.a * self.x + self.curve.b
        )

    def print_subgroup(self) -> None:
        """
        print P, [2]P, [3]P, ... until [n]P returns O.
        """
        MAX_ITERATIONS = 1000
        now = self
        print(f"P: {now}")
        for i in range(2, MAX_ITERATIONS + 1):
            now = now + self
            print(f"[{i}]P: {now}")
            if now.is_point_at_infinity:
                break

    def subgroup(self) -> list["PointOverEC"]:
        MAX_ITERATIONS = 1000
        now = self
        ret = [now]
        if now.is_point_at_infinity:
            return ret
        for _ in range(2, MAX_ITERATIONS + 1):
            now = now + self
            ret.append(now)
            if now.is_point_at_infinity:
                return ret

        raise Exception

    def __add__(self, other: Self) -> "PointOverEC":
        # 無限遠点 O は単位元
        if self.is_point_at_infinity:
            return other
        if other.is_point_at_infinity:
            return self

        # y 軸で対称なら O を返す
        if self.x == other.x and self.y == -other.y:
            return self.__class__(self.curve, x=0, y=0, is_point_at_infinity=True)

        if self == other:
            lmd = (Fp(3, self.curve.p) * self.x**2 + self.curve.a) / (
                Fp(2, self.curve.p) * self.y
            )
        else:
            lmd = (other.y - self.y) / (other.x - self.x)

        x3 = lmd**2 - self.x - other.x
        y3 = -lmd * x3 - self.y + lmd * self.x
        return self.__class__(self.curve, x=x3, y=y3)

    def __mul__(self, n: int):
        """return [n]P = P + ... + P (n-times)."""
        if isinstance(n, int):
            ret = self.id()
            tmp = self
            for i in range(n.bit_length()):
                if n >> i & 1:
                    ret += tmp
                tmp += tmp
            return ret
        raise TypeError(
            "Only scalar multiplication is defined. Do you mean pointwise addition?"
        )

    __rmul__ = __mul__

    def __str__(self) -> str:
        if self.is_point_at_infinity:
            return "(∞, ∞)"
        return f"({self.x}, {self.y})"

    __repr__ = __str__

    # def __repr__(self) -> str:
    #     return f"PointOverEC({self.x}, {self.y}, {self.is_point_at_infinity})"

    # def __format__(self, __format_spec: str) -> str:
    #     return str(self)

    def __eq__(self, other: Self) -> bool:
        return (
            self.x == other.x
            and self.y == other.y
            and self.is_point_at_infinity == other.is_point_at_infinity
        )
