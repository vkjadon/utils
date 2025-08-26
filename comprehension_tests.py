def test_q1(func):
    return all(func(x) == x**2 for x in [0, 2, -3, 10])
