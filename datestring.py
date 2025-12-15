import teststs

def dsparse(text: str):
    if text.isdecimal():
        match len(text):
            case 8:
                return int(text[0:4]), int(text[4:6]), int(text[6:8])
            case 6:
                return int(text[0:2])+2000, int(text[2:4]), int(text[4:6])
            case 4:
                return 2000, int(text[0:2]), int(text[2:4])
    for i in ["-", "/", " ", "_"]: 
        split_text = text.split(i)
        if len(split_text) == 2:
            return 2000, int(split_text[0]), int(split_text[1])
        if len(split_text[0]) == 2:
            return int(split_text[0])+2000, int(split_text[1]), int(split_text[2])
        if len(split_text[0]) == 4:
            return int(split_text[0]), int(split_text[1]), int(split_text[2])
    
    dot_split = text.split(".")
    if dot_split[-1] == "":
        match len(dot_split)-1:
            case 2:
                return 2000, int(dot_split[0]), int(dot_split[1])
            case 3:
                if len(dot_split[0]) == 2:
                    return int(dot_split[0])+2000, int(dot_split[1]), int(dot_split[2])
                if len(dot_split[0]) == 4:
                    return int(dot_split[0]), int(dot_split[1]), int(dot_split[2])
    else:
        match len(dot_split):
            case 2:
                return 2000, int(dot_split[0]), int(dot_split[1])
            case 3:
                if len(dot_split[0]) == 2:
                    return int(dot_split[0])+2000, int(dot_split[1]), int(dot_split[2])
                if len(dot_split[0]) == 4:
                    return int(dot_split[0]), int(dot_split[1]), int(dot_split[2])
    return None

if __name__ == "__main__":
    tests = [
        # 8자리 숫자
        ("20231231", (2023, 12, 31)),
        # 6자리 숫자
        ("231231", (2023, 12, 31)),
        # 4자리 숫자
        ("1231", (2000, 12, 31)),

        # YYYY-MM-DD
        ("2023-12-31", (2023, 12, 31)),
        # YY-MM-DD
        ("23-12-31", (2023, 12, 31)),
        # MM-DD
        ("12-31", (2000, 12, 31)),

        # YYYY.MM.DD
        ("2023.12.31", (2023, 12, 31)),
        # YY.MM.DD
        ("23.12.31", (2023, 12, 31)),
        # MM.DD
        ("12.31", (2000, 12, 31)),

        # YYYY.MM.DD.
        ("2023.12.31.", (2023, 12, 31)),
        # YY.MM.DD.
        ("23.12.31.", (2023, 12, 31)),
        # MM.DD.
        ("12.31.", (2000, 12, 31)),

        # YYYY/MM/DD
        ("2023/12/31", (2023, 12, 31)),
        # YY/MM/DD
        ("23/12/31", (2023, 12, 31)),
        # MM/DD
        ("12/31", (2000, 12, 31)),

        # YYYY MM DD
        ("2023 12 31", (2023, 12, 31)),
        # YY MM DD
        ("23 12 31", (2023, 12, 31)),
        # MM DD
        ("12 31", (2000, 12, 31)),

        # YYYY_MM_DD
        ("2023_12_31", (2023, 12, 31)),
        # YY_MM_DD
        ("23_12_31", (2023, 12, 31)),
        # MM_DD
        ("12_31", (2000, 12, 31)),
    ]

    teststs.testtest(tests, dsparse)