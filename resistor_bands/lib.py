"""4/5-band decode, inverse, E-series, series/parallel hunt for a target."""
from __future__ import annotations

COLORS = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
E24 = [
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
    3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
]


def ohms(b1: str, b2: str, mult: str) -> float:
    d1, d2 = COLORS.index(b1), COLORS.index(b2)
    m = 0.1 if mult == "gold" else 0.01 if mult == "silver" else 10 ** COLORS.index(mult)
    return (d1 * 10 + d2) * m


def ohms5(b1: str, b2: str, b3: str, mult: str) -> float:
    d = COLORS.index(b1) * 100 + COLORS.index(b2) * 10 + COLORS.index(b3)
    m = 0.1 if mult == "gold" else 0.01 if mult == "silver" else 10 ** COLORS.index(mult)
    return d * m


def inverse(target: float) -> dict:
    best = None
    for a in COLORS:
        for b in COLORS:
            for m in list(COLORS) + ["gold", "silver"]:
                v = ohms(a, b, m)
                err = abs(v - target)
                if best is None or err < best["err"]:
                    best = {"bands": [a, b, m], "ohms": v, "err": err}
    return best


def e24_near(target: float) -> dict:
    if target <= 0:
        return {"ohms": 0, "decade": 0}
    decade = 10 ** max(0, int(round(math_log10(target))) - 1)
    # keep simple
    import math

    exp = math.floor(math.log10(target))
    decade = 10**exp
    mant = target / decade
    closest = min(E24, key=lambda x: abs(x - mant))
    return {"ohms": closest * decade, "series": "E24", "err": abs(closest * decade - target)}


def math_log10(x: float) -> float:
    import math

    return math.log10(x)


def combine(target: float, pool: list[float] | None = None) -> dict:
    """Find series or parallel of two E24 values closest to target."""
    import math

    vals = []
    for e in range(2, 7):
        for m in E24:
            vals.append(m * 10**e)
    pool = pool or vals
    best = {"how": "single", "parts": [], "ohms": 0, "err": 1e18}
    for a in pool:
        err = abs(a - target)
        if err < best["err"]:
            best = {"how": "single", "parts": [a], "ohms": a, "err": err}
        for b in pool:
            s = a + b
            p = (a * b) / (a + b) if (a + b) else 0
            for how, v in (("series", s), ("parallel", p)):
                e = abs(v - target)
                if e < best["err"]:
                    best = {"how": how, "parts": [a, b], "ohms": v, "err": e}
    return best
