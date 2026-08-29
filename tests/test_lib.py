from resistor_bands.lib import combine, e24_near, inverse, ohms


def test_10k():
    assert ohms("brown", "black", "orange") == 10000
    assert inverse(10000)["ohms"] == 10000
    assert e24_near(10000)["ohms"] == 10000
    assert combine(15000)["err"] < 100
