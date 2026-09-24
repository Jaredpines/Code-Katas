def hamming(n):
    h = [1]
    i2 = i3 = i5 = 0
    
    while len(h) < n:
        nextNum = min(h[i2] * 2, h[i3] * 3, h[i5] * 5)
        h.append(nextNum)
        
        if nextNum == h[i2] * 2:
            i2 += 1
        
        if nextNum == h[i3] * 3:
            i3 += 1
        
        if nextNum == h[i5] * 5:
            i5 += 1
    
    return h[-1]