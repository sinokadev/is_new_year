def run_test(tests, func):
    for value, expected in tests:
        result = func(value)
        if result != expected:
            return False, value, expected, result
    return True, None, None, None

def testtest(tests, func):
    result = run_test(tests, func)
    if not result[0]: print("Your code is shit", "input:", result[1], "expected:", result[2], "actual", result[3])
    else: print("OK!")