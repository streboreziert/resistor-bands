COLORS = ("black","brown","red","orange","yellow","green","blue","violet","grey","white")

def ohms(b1, b2, mult):
    d1, d2 = COLORS.index(b1), COLORS.index(b2)
    m = 0.1 if mult == "gold" else 0.01 if mult == "silver" else 10 ** COLORS.index(mult)
    return (d1 * 10 + d2) * m

def ohms5(b1, b2, b3, mult):
    d = COLORS.index(b1) * 100 + COLORS.index(b2) * 10 + COLORS.index(b3)
    m = 0.1 if mult == "gold" else 0.01 if mult == "silver" else 10 ** COLORS.index(mult)
    return d * m

def inverse(target):
    best = None
    for a in COLORS:
        for b in COLORS:
            for m in list(COLORS) + ["gold", "silver"]:
                try:
                    v = ohms(a, b, m)
                except ValueError:
                    continue
                err = abs(v - target)
                if best is None or err < best["err"]:
                    best = {"bands": [a, b, m], "ohms": v, "err": err}
    return best
