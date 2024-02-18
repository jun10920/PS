from collections import deque
def solution(prog, speeds):
    
    dayLeft = deque()
    for p, s in zip(prog, speeds):
        dayLeft.append(-((p - 100) // s))
    print(dayLeft)
    answer = []
    
    while dayLeft:
        count = 1
        first = dayLeft.popleft()
        while dayLeft and first >= dayLeft[0]:
            dayLeft.popleft()
            count +=1
        answer.append(count)
    return answer