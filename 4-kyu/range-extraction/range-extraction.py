def solution(args):
    result = []
    i = 0
    
    while i < len(args):
        start = args[i]
        while i + 1 < len(args) and args[i + 1] == args[i] + 1:
            i += 1
        end = args[i]
        
        if end - start >= 2:
            result.append(f"{start}-{end}")
        elif end - start == 1:
            result.append(str(start))
            result.append(str(end))
        else:
            result.append(str(start))
            
        i += 1
        
    return ",".join(result)