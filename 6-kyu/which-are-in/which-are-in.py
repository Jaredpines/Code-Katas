def in_array(array1, array2):
    sub = []
    for w in array1:
        for w2 in array2:
            if w in w2 and w not in sub:
                sub.append(w)
    sub.sort()
    return sub