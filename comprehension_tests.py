def test_q1(func):
  return (func("Vijay") == ["v", "j", "y"] and func("Mechanical") == ["m", "c", "a", "i", "a"])

def test_q2(func):
  return (func([5, 7, -9, 8, 0]) == [25, 81, 0])

def test_q3(func) :
  return func(sentence) == ['quick', 'brown', 'jumps', 'over', 'lazy']

