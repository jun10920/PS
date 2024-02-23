def solution(p):
    answer = [0] * len(p)
    stack = []
    
    for i, v in enumerate(p):
        while stack and v < p[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = len(p) - 1 - j
    
    return answer