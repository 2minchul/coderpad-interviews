from itertools import islice
from typing import List, Tuple

Interval = Tuple[int, int]
Intervals = List[Interval]


def merge_two_interval(a: Interval, b: Interval) -> Intervals:
    """
    a[0] <= b[0] 일때 a와 b를 합친 intervals
    """
    if a[1] < b[0]:
        return [a, b]

    return [(a[0], max(a[1], b[1]))]


def merge(intervals: Intervals) -> Intervals:
    intervals.sort()
    result: Intervals = []
    before = intervals[0]

    for interval in islice(intervals, 1, None):
        *a, before = merge_two_interval(before, interval)
        result.extend(a)
    result.append(before)

    return result
