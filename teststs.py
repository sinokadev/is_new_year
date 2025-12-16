def run_test(tests, func):
    for test in tests:
        result = func(test[0])
        if result != test[1]:
            return False, test[0], result
        print("OK!", test[0], result)
    return True, "", ""

def testtest(tests, func):
    result = run_test(tests, func)
    if not result[0]: print("Your code is shit", result[1], result[2])
    else: print("OK!")