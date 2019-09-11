def test_p77_merge():
    from .p77 import merge
    _test_merge(merge)


def test_my_solution_merge():
    from .my_solution import merge
    _test_merge(merge)


def _test_merge(merge):
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]
