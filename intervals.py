def merge_intervals(intervals):
    """Merge overlapping or adjacent intervals.
    merge_intervals([(1, 3), (2, 5), (8, 10)]) -> [(1, 5), (8, 10)]
    merge_intervals([(1, 5), (2, 3)])          -> [(1, 5)]
    Each interval is (start, end) with start <= end.
    """
    if not intervals:
        return []
    ordered = sorted(intervals)
    result = [ordered[0]]
    for start, end in ordered[1:]:
        last_start, last_end = result[-1]
        if start <= last_end + 1:          # overlapping or adjacent
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))
    return result
