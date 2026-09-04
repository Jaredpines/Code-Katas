from collections import Counter
import string
def duplicate_encode(word):
    par = word.lower()
    char = set(string.ascii_lowercase) - set(par)
    char1 = sorted(char)[0]
    char2 = sorted(char)[1]
    if "(" in word:
        par = par.replace("(", char1)
    if ")" in word:
        par = par.replace(")", char2)
    textCount = Counter(list(par))
    for key, value in textCount.items():
        if value > 1:
            par = par.replace(key, ")")
        else:
            par = par.replace(key, "(")
    
    return par