from EC.Fp import Fp


class EllipticCurve:
    """
    Elliptic Curve Class over Fp

    E/Fp の Python 実装

    ## パラメータ
    - `p`: Fp の p
    - `a, b` : Fp の元
    """

    def __init__(self, p, a: Fp, b: Fp):
        self.p = p
        self.a = a
        self.b = b

    @property
    def j_invariant(self) -> Fp:
        """calculate the j-invariant of the curve."""
        return 1728 * (4 * self.a**3) / (4 * self.a**3 + 27 * self.b**2)

    def is_singular(self) -> bool:
        """If given curve is singular, then return True."""
        return 4 * self.a.x**3 + 27 * self.b.x**2 == 0

    def __eq__(self, other):
        return self.p == other.p and self.a == other.a and self.b == other.b

    def __str__(self):
        return f"Y^2 = X^3 + {self.a}X + {self.b}"
