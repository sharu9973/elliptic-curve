from EC.EllipticCurve import EllipticCurve
from EC.Fp import Fp
from EC.PointOverEC import PointOverEC

from EC.isogeny import E_over_G, isogeny


class TestIsogeny:
    prime = 7
    a = Fp(0, prime)
    b = Fp(1, prime)
    curve = EllipticCurve(prime, a, b)

    def test_velu1(self):
        p = PointOverEC(self.curve, Fp(3, self.prime), Fp(0, self.prime))
        assert p.is_valid()

        # (3, 0) で生成される部分群 G = {(3, 0), O}
        subgroups = p.subgroup()
        new_curve = E_over_G(self.curve, subgroups)
        print(self.curve, "-->", new_curve)
        assert new_curve == EllipticCurve(self.prime, 5, 1)

    def test_velu2(self):
        points: list[PointOverEC] = []
        for i in range(self.prime):
            for j in range(self.prime):
                point = PointOverEC(self.curve, Fp(i, self.prime), Fp(j, self.prime))
                if point.is_valid():
                    points.append(point)

        for point in points:
            subgroup = point.subgroup()
            new_curve = E_over_G(self.curve, subgroup)
            print(subgroup, new_curve)
            for sp in points:
                if sp in subgroup:
                    continue
                print("\t", sp, "goes to", isogeny(sp, self.curve, subgroup))
