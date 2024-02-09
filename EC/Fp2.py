from .Fp import Fp


class Fp2:
    def __init__(self, a: Fp, b: Fp):
        """"""
        if a.p != b.p:
            raise ValueError(
                f"Should be same base field; a in F{a.p}, but b in F{b.p}."
            )
        self.a = a
        self.b = b
        self.p = a.p
        self.ch = self.p
        self.order = a.p**2
        self.beta_sq = self.get_quadratic_non_residue()

    def get_quadratic_non_residue(self) -> Fp:
        """Fp 上平方非剰余な元を返す"""
        # if p = 3 mod 4, then -1 is a quadratic non residue
        if self.ch % 4 == 3:
            return Fp(self.ch - 1, self.p)

        # Otherwise, find a quadratic non residue
        if self.ch % 4 == 1:
            for i in range(2, self.p):
                if not self.is_quadratic_residue(i):
                    return Fp(i, self.p)

    def is_quadratic_residue(self, x: int) -> bool:
        """x in Fp が Fp 上平方剰余かどうかを返す"""
        w = pow(x, (self.ch - 1) // 2, self.ch)
        return 1 == w

    def __add__(self, other: "Fp2") -> "Fp2":
        return self.__class__(self.a + other.a, self.b + other.b)

    def __mul__(self, other: "Fp2") -> "Fp2":
        x = self.a * other.a + self.b * other.b * self.beta_sq
        y = self.b * other.a + self.a * other.b
        return self.__class__(x, y)

    def __eq__(self, other: "Fp2"):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        return f"({self.a}, {self.b})"
