from EC.EllipticCurve import EllipticCurve
from EC.PointOverEC import PointOverEC
from EC.Fp import Fp


def E_over_G(E: EllipticCurve, G: list[PointOverEC]) -> EllipticCurve:
    """
    calculate new curve with Velu's formula.
    G is a finite subgroup of E(\\bar{k})
    """
    u = Fp(0, E.p)
    v = Fp(0, E.p)
    for q in G:
        if q.is_point_at_infinity:
            continue
        u += 3 * q.x**2 + E.a
        v += 5 * q.x**3 + 3 * E.a * q.x + E.b

    new_a = E.a - 5 * u
    new_b = E.b - 7 * v
    return EllipticCurve(E.p, new_a, new_b)


def isogeny(P: PointOverEC, E: EllipticCurve, G: list[PointOverEC]) -> PointOverEC:
    """
    return phi(P) s.t. phi: E -> E/G
    """

    x = P.x
    y = P.y
    for Q in G:
        if Q.is_point_at_infinity:
            continue
        R = P + Q
        x += R.x - Q.x
        y += R.y - Q.y
    return PointOverEC(E, x, y)
