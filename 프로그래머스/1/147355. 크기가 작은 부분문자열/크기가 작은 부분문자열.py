def solution(t, p):
    temp = []
    for i in range(0, len(t) -len(p) + 1):
        temp.append(t[i:i+len(p)])
    
    answer = 0
    for i in temp:
        p = int(p)
        if int(i) <= p:
            answer += 1
    return answer