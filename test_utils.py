import pytest
from utils import clamp, merge_sorted, parse_pair, unique_sorted


# ---------------- clamp ----------------

def test_clamp_inside():
    assert clamp(5, 0, 10) == 5

def test_clamp_below():
    assert clamp(-3, 0, 10) == 0

def test_clamp_above():
    assert clamp(15, 0, 10) == 10

def test_clamp_on_lower_boundary():
    assert clamp(0, 0, 10) == 0

def test_clamp_on_upper_boundary():
    assert clamp(10, 0, 10) == 10

def test_clamp_lo_equals_hi():
    assert clamp(5, 3, 3) == 3   # peste -> hi
    assert clamp(1, 3, 3) == 3   # sub  -> lo
    assert clamp(3, 3, 3) == 3   # exact


# ---------------- merge_sorted ----------------

def test_merge_normal():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_first_empty():
    assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]

def test_merge_second_empty():
    assert merge_sorted([1, 2, 3], []) == [1, 2, 3]

def test_merge_both_empty():
    assert merge_sorted([], []) == []

def test_merge_duplicates_across():
    assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


# ---------------- parse_pair ----------------

def test_parse_pair_valid():
    assert parse_pair("3:4") == (3, 4)

def test_parse_pair_negative():
    assert parse_pair("-1:5") == (-1, 5)

def test_parse_pair_no_separator():
    with pytest.raises(ValueError):
        parse_pair("hello")

def test_parse_pair_too_many_parts():
    with pytest.raises(ValueError):
        parse_pair("1:2:3")

def test_parse_pair_not_an_int():
    with pytest.raises(ValueError):
        parse_pair("a:b")

def test_parse_pair_empty_part():
    with pytest.raises(ValueError):
        parse_pair("1:")


# ---------------- unique_sorted (expune bug-ul) ----------------

def test_unique_sorted_basic():
    # trece chiar și cu bug-ul: input "evident"
    assert unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]

def test_unique_sorted_two_duplicates():
    # trece din intamplare: doar 2 identice la rand
    assert unique_sorted([1, 1]) == [1]

def test_unique_sorted_triple_duplicate():
    # PICA cu codul buggy: 3 identice la rand -> intoarce [1, 1]
    assert unique_sorted([1, 1, 1]) == [1]

def test_unique_sorted_many_duplicates():
    # PICA cu codul buggy: 4 identice -> intoarce [5, 5]
    assert unique_sorted([5, 5, 5, 5]) == [5]
