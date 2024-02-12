def solution(part, comp):
    part.sort()
    comp.sort()
    for a,b in zip(part, comp):
        if a != b:
            return a
    return part[-1]