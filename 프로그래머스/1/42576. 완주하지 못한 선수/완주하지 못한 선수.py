def solution(part, comp):
    part.sort()
    comp.sort()
    
    for p, c in zip(part, comp):
        if p != c:
            return p
    
    return part[-1]
    
