from typing import Self


class Fp:
    def __init__(self, x: int, p: int):
        self.x = x
        self.p = p

    def __neg__(self):
        return self.__class__((-self.x) % self.p, p=self.p)

    def __add__(self, other: Self | int):
        if isinstance(other, Fp):
            # Fp + Fp -> Fp
            return self.__class__((self.x + other.x) % self.p, p=self.p)
        if isinstance(other, int):
            # int + Fp -> Fp
            # Fp + int -> Fp
            return self.__class__((self.x + other) % self.p, p=self.p)

    __radd__ = __add__

    def __sub__(self, other: Self | int):
        if isinstance(other, Fp):
            # Fp - Fp -> Fp
            return self.__class__((self.x - other.x) % self.p, p=self.p)
        if isinstance(other, int):
            # Fp - int -> Fp
            # int - Fp -> Fp
            return self.__class__((self.x - other) % self.p, p=self.p)

    __rsub__ = __add__

    def __mul__(self, other: Self | int):
        if isinstance(other, Fp):
            # Fp * Fp -> Fp
            return self.__class__((self.x * other.x) % self.p, p=self.p)
        if isinstance(other, int):
            # scolar multiplication
            # int * Fp -> Fp
            # Fp * int -> Fp
            return self.__class__((self.x * other) % self.p, p=self.p)

        raise TypeError

    __rmul__ = __mul__

    def __truediv__(self, other: Self | int):
        # a / b = a * b^-1
        inv = pow(other.x, -1, self.p)
        return self * Fp(inv, self.p)

    def __pow__(self, modulo: int):
        # a ** e
        res = pow(self.x, modulo, self.p)
        return self.__class__(res, p=self.p)

    def __eq__(self, other: Self | int) -> bool:
        if isinstance(other, Fp):
            return self.x == other.x
        if isinstance(other, int):
            return self.x == other

    def __repr__(self) -> str:
        return f"Fp({self.x}, {self.p})"

    def __format__(self, __format_spec: str) -> str:
        return str(self)

    def __str__(self):
        return f"{self.x}"
