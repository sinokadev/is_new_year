import teststs
import isnewyear

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
if not result[0]: print("Your code is shit", result[1])
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
if not result[0]: print("Your code is shit", result[1])
else: print("OK!")

print("----[English]----")

tests = [
["January 1", True],
["January 1 2025", True],
["January 1st", True],
["January 1st 1999", True],
["January first", True],
["January first 2050", True],
["Jan 1", True],
["Jan. 1", True],
["Jan 1 3000", True],
["1 January", True],
["1 January 2023", True],
["1st January", True],
["1st January 2000", True],
["first January", True],
["first January 2022", True],
["the first of January", True],
["the first of January 2025", True],
["New Year's Day", True],
["New Year's Day 2023", True],

# False cases
["January 2", False],
["on January 1", False],
["Jan 1st something", False],
["something 1 January", False],
["the first of January something", False],
["January first!", False],
["Jan. 1,", False],
]

result = teststs.run_test(tests, isnewyear)
if not result[0]:print("Your code is shit", result[1])
else: print("OK!")
