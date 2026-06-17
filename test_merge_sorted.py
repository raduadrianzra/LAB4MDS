from merge_sorted import merge_sorted

def test_normal():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_first_empty():
    assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]

def test_second_empty():
    assert merge_sorted([1, 2, 3], []) == [1, 2, 3]

def test_both_empty():
    assert merge_sorted([], []) == []

def test_duplicates():
    assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]
