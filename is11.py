import re

def is11(text):
    # Korean
    pattern = re.compile(r'^(?:(\d+)\s*년\s*)?(\d+)\s*월\s*(\d+)\s*일$')
    m = pattern.fullmatch(text)
    if not m:
        return False
    year, month, day = m.groups()
    return int(month) == 1 and int(day) == 1

# Test
print(is11("1월 1일"))
print(is11("ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 1월 1일"))
print(is11("ㅇㄻㄻㄴㅇㄻㄴㄹㅇㅁㅇㄴ 5월 1일"))
print(is11("5월 6일"))
print(is11("5000년 1월 1일"))
print(is11("503224200년 1월 1일"))
print(is11("5000년 1월 5일"))
print(is11("503224200년 5월 1일"))