from resistor_bands.lib import ohms, inverse

def test_10k():
    assert ohms("brown", "black", "orange") == 10000
    assert inverse(10000)["ohms"] == 10000
