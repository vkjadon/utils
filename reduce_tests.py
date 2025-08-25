def test_q1(func):
    return all(func(x) == x**2 for x in [0, 2, -3, 10])
    
def run_tests():
    assert q1(12345) == 15
    assert q1(999) == 27

    assert q2([2, 3, 4]) == 24
    assert q2([1, 5, 6]) == 30

    assert q3([56, 89, 23, 90, 67]) == 90
    assert q4([12, 4, 19, 3, 7]) == 3

    assert q5(["Data", "Science", "is", "fun"]) == "DataScienceisfun"
    
    assert q6([2, 4, 6, 8]) == True
    assert q6([2, 5, 6]) == False

    assert q7([48, 64, 80]) == 16
    assert q7([12, 18, 24]) == 6

    assert q8(["AI", "Artificial", "Robotics", "ML"]) == "Artificial"
    
    assert q9([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

    assert q10("bananas") == 3
    assert q10("apple") == 1

    print("🎉 All tests passed successfully!")

# Run all tests
run_tests()
