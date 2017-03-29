import thelibrary as t

def test_calculation_positive():
    assert t.calculation(1, 2, 3) == 6
    assert t.calculation(0, 20, 3) == 23

def test_calculation_negative():
    assert t.calculation(-1, -2, 3) == 0
    assert t.calculation(-1, -2, -100) == -103

def test_calculation_bordercase():
    assert t.calculation(0, 0, 0) == 0

def test_calculation_floats():
    assert t.calculation(0.5, 0.5, 1.) == 2.0
