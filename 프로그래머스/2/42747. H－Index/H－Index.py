def solution(c):
    c.sort(reverse = True)
    answer = 0
    for i, v in enumerate(c):
        if v >= i + 1:
            answer = i + 1
            
    if c[-1] > len(c):
        answer =len(c)
    
    return answer