def run_test(tests, func):
    for value, expected in tests:
        result = func(value)
        if result != expected:
            return False, value, expected, result
    return True, None, None, None

def testtest(tests, func, detail = False):
    result = run_test(tests, func)
    if detail:
        if not result[0]: 
            print("Your code is shit\n", "input:", result[1], ", expected:", result[2], ", actual", result[3])
            return
    else:
        if not result[0]: 
            print("Your code is shit", result[1], result[3])
            return
    print("OK!")