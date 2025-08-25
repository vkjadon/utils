def test_q1(func):
    return all(func(x) == x**2 for x in [0, 2, -3, 10])

def test_q2(func):
    return all(func(x) == (x%2==0) for x in range(-5,6))

def test_q3(func):
    return all(func(a,b) == max(a,b) for a,b in [(1,2),(5,3),(-1,-5),(0,0)])

def test_q4(func):
    return all(func(s) == s[::-1] for s in ["abc","racecar","","hello"])

def test_q5(func):
    return all(func(n) == sum(int(d) for d in str(n)) for n in [123,405,999,0])

def test_q6(func):
    import math
    return all(func(n) == math.factorial(n) for n in range(0,7))

def test_q7(func):
    return all(func(s) == (s==s[::-1]) for s in ["madam","abc","racecar",""])

def test_q8(func):
    return all(func(a,b,c) == min(a,b,c) for a,b,c in [(1,2,3),(5,3,9),(-1,0,-2),(0,0,0)])

def test_q9(func):
    return func("hello") == 2 and func("xyz") == 0 and func("AEIOU") == 5

def test_q10(func):
    return func([(1,3),(2,1),(5,2)]) == [(2,1),(5,2),(1,3)]
