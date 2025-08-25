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
    
def test_q11(func):
    return func(1200) == 1080 and func(800) == 800

def test_q12(func):
    return func(15) == True and func(12) == False and func(19) == True

def test_q13(func):
    plots = [(2,3),(4,5),(1,10)]
    return func(plots) == (4,5)

def test_q14(func):
    return func(35) == "Fail" and func(50) == "Pass"

def test_q15(func):
    return func(3) == 50 and func(10) == 100

def test_q16(func):
    return func(0) == 32 and func(100) == 212

def test_q17(func):
    return func(95)=="A" and func(80)=="B" and func(60)=="C" and func(40)=="C" and func(30)=="F"

def test_q18(func):
    return func(10)==True and func(20)==False and func(9)==True and func(18)==True

def test_q19(func):
    words = ["madam","racecar","apple","level"]
    return func(words) == ["madam","racecar","level"]

def test_q20(func):
    emps = [("A",5000),("B",8000),("C",7000)]
    return func(emps) == [("B",8000),("C",7000),("A",5000)]
