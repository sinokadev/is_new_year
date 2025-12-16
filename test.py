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
teststs.testtest(tests, isnewyear.isnewyear)

print("----[Unix-time]----")

# Test / Unix-time
tests = [
[1767225600, True],
[1767222348, False],
[1767229348, True],
[1762342348, False],
]
teststs.testtest(tests, isnewyear.isnewyear)
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

teststs.testtest(tests, isnewyear.isnewyear)

print("----[Date String]----")

tests = [
    # 8자리 숫자
    ("20230101", True),
    ("20231231", False),
    # 6자리 숫자
    ("230101", True),
    ("231231", False),
    # 4자리 숫자
    ("0101", True),
    ("1231", False),

    # YYYY-MM-DD
    ("2023-01-01", True),
    ("2023-12-31", False),
    # YY-MM-DD
    ("23-01-01", True),
    ("23-12-31", False),
    # MM-DD
    ("01-01", True),
    ("12-31", False),

    # YYYY.MM.DD
    ("2023.01.01", True),
    ("2023.12.31", False),
    # YY.MM.DD
    ("23.01.01", True),
    ("23.12.31", False),
    # MM.DD
    ("01.01", True),
    ("12.31", False),

    # YYYY.MM.DD.
    ("2023.01.01.", True),
    ("2023.12.31.", False),
    # YY.MM.DD.
    ("23.01.01.", True),
    ("23.12.31.", False),
    # MM.DD.
    ("01.01.", True),
    ("12.31.", False),

    # YYYY/MM/DD
    ("2023/01/01", True),
    ("2023/12/31", False),
    # YY/MM/DD
    ("23/01/01", True),
    ("23/12/31", False),
    # MM/DD
    ("01/01", True),
    ("12/31", False),

    # YYYY MM DD
    ("2023 01 01", True),
    ("2023 12 31", False),
    # YY MM DD
    ("23 01 01", True),
    ("23 12 31", False),
    # MM DD
    ("01 01", True),
    ("12 31", False),

    # YYYY_MM_DD
    ("2023_01_01", True),
    ("2023_12_31", False),
    # YY_MM_DD
    ("23_01_01", True),
    ("23_12_31", False),
    # MM_DD
    ("01_01", True),
    ("12_31", False),
]

teststs.testtest(tests, isnewyear.isnewyear)

print("----[ISO 8601]----")

tests = [
    # True cases - 1월 1일
    ["2026-01-01T00:00:00Z", True],
    ["2025-01-01T12:30:45Z", True],
    ["1999-01-01T23:59:59Z", True],
    ["2026-01-01T00:00:00+00:00", True],
    ["2026-01-01T09:00:00+09:00", True],  # 타임존 다른 경우
    ["2026-01-01T00:00:00.000Z", True],  # 밀리초 포함
    ["2026-01-01T00:00:00", True],  # Z 없는 경우

    # False cases - 1월 1일 아님
    ["2026-01-02T00:00:00Z", False],
    ["2026-02-01T00:00:00Z", False],
    ["2026-12-31T23:59:59Z", False],
    ["2025-03-15T12:00:00Z", False],
    ["2026-01-01T00:00:00ZABC", False],  # 뒤에 이상한 거 붙음
    ["ABC2026-01-01T00:00:00Z", False],  # 앞에 이상한 거 붙음
    ["2026/01/01T00:00:00Z", False],  # 잘못된 구분자
]

teststs.testtest(tests, isnewyear.isnewyear)