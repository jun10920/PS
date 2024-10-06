import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    leftDays = []
    
    for p, s in zip(progresses, speeds):
        temp = math.ceil((100 - p) / s) 
        leftDays.append(temp)
    
    leftDays = deque(leftDays)
    
    while leftDays:
        temp = leftDays.popleft()
        cnt = 1
        while leftDays and leftDays[0] <= temp:
            leftDays.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer