def run_test(tests, func):
    for test in tests:
        if func(test[0]) != test[1]:
            return False, test[0]
    return True, ""