import datetime

def parse_date(value: str) -> datetime.date | None:
    if not isinstance(value, str):
        return None

    formats = [
        "%Y-%m-%dT%H:%M:%S.%f%z",  # 밀리초 + TZ
        "%Y-%m-%dT%H:%M:%S%z",     # TZ
        "%Y-%m-%dT%H:%M:%S",       # 시간만
        "%Y-%m-%d",                # 날짜만
    ]

    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(value, fmt)
            return dt.date()
        except ValueError:
            continue

    return None
