# test_runner.py
import importlib.util
import sys

def load_tests(path="tests_file.py"):
    """Dynamically load test file (default: tests_file.py)"""
    spec = importlib.util.spec_from_file_location("tests", path)
    tests = importlib.util.module_from_spec(spec)
    sys.modules["tests"] = tests
    spec.loader.exec_module(tests)
    return tests

def check_solution(func, qnum, tests):
    """Run a solution against a given test number"""
    test_func = getattr(tests, f"test_q{qnum}")
    return test_func(func)

def report_solution(status):
    if status:
        print(f"\033[92m: ✅ All Test Cases Passed\033[0m")   # Green
    else:
        print(f"\033[91m: ❌ Some Test Cases Failed\033[0m")  # Red
