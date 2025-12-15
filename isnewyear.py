import re
import datetime
import datestring

def isnewyear(value):
    if type(value) == str:
        value = value.strip()

        # Korean
        korean_pattern = re.compile(r'^(?:(\d+)년\s*)?(\d+)월\s*(\d+)일$')
        m = korean_pattern.fullmatch(value)
        if m:
            _, month, day = m.groups()
            if int(month) == 1 and int(day) == 1:
                return True

        # English
        text = value.strip().lower()
        
        english_patterns = [
            r'^(january|jan\.?)\s+(1|1st|first)(\s+\d+)?$',     # January 1 / Jan 1 / ... + optional year
            r'^(1|1st|first)\s+(january|jan\.?)(\s+\d+)?$',     # 1 January / first January + optional year
            r'^the\s+first\s+of\s+(january|jan\.?)(\s+\d+)?$',  # the first of January + optional year
            r"^new\s*year'?s\s*day(\s+\d+)?$"                   # New Year's Day + optional year
        ]
        
        if any(re.match(pattern, text) for pattern in english_patterns):
            return True
        
        if datestring.dsparse(value):
            if datestring.dsparse(value)[1] == datestring.dsparse(value)[2] == 1:
                return True
    elif type(value) == int:
        dt = datetime.datetime.fromtimestamp(value, datetime.timezone.utc)
        if dt.month == 1 and dt.day == 1:
            return True
    return False