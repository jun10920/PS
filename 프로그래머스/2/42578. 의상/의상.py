from collections import Counter
def solution(c): 
    arr = Counter([i[1] for i in c])
    answer = 1
    for i in arr.values():
        answer *= (i+1)

    return answer -1