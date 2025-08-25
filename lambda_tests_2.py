# tests_lambda.py

def test_q1(func):
    return func(1200) == 1080 and func(800) == 800

def test_q2(func):
    return func(15) == True and func(12) == False and func(19) == True

def test_q3(func):
    plots = [(2,3),(4,5),(1,10)]
    return func(plots) == (4,5)

def test_q4(func):
    return func(35) == "Fail" and func(50) == "Pass"

def test_q5(func):
    return func(3) == 50 and func(10) == 100

def test_q6(func):
    return func(0) == 32 and func(100) == 212

def test_q7(func):
    return func(95)=="A" and func(80)=="B" and func(60)=="C" and func(40)=="C" and func(30)=="F"

def test_q8(func):
    return func(10)==True and func(20)==False and func(9)==True and func(18)==True

def test_q9(func):
    words = ["madam","racecar","apple","level"]
    return func(words) == ["madam","racecar","level"]

def test_q10(func):
    emps = [("A",5000),("B",8000),("C",7000)]
    return func(emps) == [("B",8000),("C",7000),("A",5000)]
