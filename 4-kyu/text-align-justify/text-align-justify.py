import textwrap
def justify(text, width):
    if text == "":
        return text
    
    wrap = textwrap.wrap(text, width = width)
    
    justifiedLines = []
    
    for i, line in enumerate(wrap):
        words = line.split()
        
        if i == len(wrap) - 1 or len(words) <= 1:
            justifiedLines.append(" ".join(words))
            continue
        
        gaps = [" "] * (len(words) - 1)
        
        currentLen = sum(len(w) for w in words) + len(gaps)
        
        idx = 0
        while currentLen < width:
            gaps[idx] += " "
            currentLen += 1
            idx = (idx + 1) % len(gaps)
        
        justifiedLine = ""
        for j in range(len(gaps)):
            justifiedLine += words[j] + gaps[j]
        justifiedLine += words[-1]
        
        justifiedLines.append(justifiedLine)
    
    return "\n".join(justifiedLines)