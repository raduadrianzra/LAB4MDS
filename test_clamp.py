from clamp import clamp

def test_inside():
    assert clamp(5, 0, 10) == 5

def test_below():
    assert clamp(-3, 0, 10) == 0

def test_above():
    assert clamp(15, 0, 10) == 10

def test_lower_boundary():
    assert clamp(0, 0, 10) == 0

def test_upper_boundary():
    assert clamp(10, 0, 10) == 10

def test_degenerate_range_collapses_to_hi():
    # lo > hi: omoara mutantul `x < lo` -> `x <= lo`
    assert clamp(5, 5, 3) == 3
    assert clamp(0, 0, -2) == -2
