from collections import Counter
def first_non_repeating_letter(s):
    first = ""
    countText = Counter(list(s.lower()))
    for key, value in countText.items():
        if value == 1:
            if key in s:
                first = key
            else:
                first = key.upper()
            break
    return first
