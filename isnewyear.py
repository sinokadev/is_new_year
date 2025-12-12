import re
import datetime
import teststs

def isnewyear(value):
    if type(value) == str:
        # Korean
        pattern = re.compile(r'^(?:(\d+)년\s*)?(\d+)월\s*(\d+)일$')
        m = pattern.fullmatch(value)
        if not m:
            return False
        year, month, day = m.groups()
        return int(month) == 1 and int(day) == 1
    elif type(value) == int:
        dt = datetime.datetime.fromtimestamp(value, datetime.timezone.utc)
        if dt.month == 1 and dt.day == 1:
            return True
        else: return False

if __name__ == "__main__":
    print("----[Test]----")
    print("How To Use")
    print("Just run")

    # Test / Korean
    print("----[Korean]----")

    tests = [
        ["1월 1일", True],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 1월 1일", False],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 5월 1일", False],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 1월 5일", False],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 205년 5월 1일", False],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 2055년 1월 5일", False],
        ["ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 2055년 1월 1일", False],
        ["5000년 1월 1일", True],
        ["503224200년 1월 1일", True],
        ["5000년 1월 5일", False],
        ["503224200년 5월 1일", False]
    ]
    result = teststs.run_test(tests, isnewyear)
    if not result[0]:
        print("Your code is shit", result[1])
    else: print("OK!")

    print("----[Unix-time]----")

    # Test / Unix-time
    tests = [
        [1767225600, True],
        [1767222348, False],
        [1767229348, True],
        [1762342348, False],
    ]
    result = teststs.run_test(tests, isnewyear)
    if not result[0]:
        print("Your code is shit", result[1])
    else: print("OK!")