from hypothesis import given, assume
from hypothesis import strategies as st
from utils import clamp, merge_sorted



@given(st.integers(), st.integers(), st.integers())
def test_clamp_in_bounds(x, lo, hi):
    assume(lo <= hi)
    result = clamp(x, lo, hi)
    assert lo <= result <= hi

@given(st.integers(), st.integers(), st.integers())
def test_clamp_idempotent(x, lo, hi):
    assume(lo <= hi)
    once = clamp(x, lo, hi)
    assert clamp(once, lo, hi) == once

@given(st.integers(), st.integers(), st.integers())
def test_clamp_noop_when_in_range(x, lo, hi):
    assume(lo <= hi)
    assume(lo <= x <= hi)
    assert clamp(x, lo, hi) == x
    

sorted_lists = st.lists(st.integers()).map(sorted)

@given(sorted_lists, sorted_lists)
def test_merge_result_is_sorted(a, b):
    result = merge_sorted(a, b)
    assert result == sorted(result)

@given(sorted_lists, sorted_lists)
def test_merge_length(a, b):
    assert len(merge_sorted(a, b)) == len(a) + len(b)

@given(sorted_lists, sorted_lists)
def test_merge_is_permutation(a, b):
    assert sorted(merge_sorted(a, b)) == sorted(a + b)
