from collections import deque

def solution(prog, speeds):
    answer = []
    queue1 = deque()
    queue2 = deque()
    for i in prog:
        queue1.append(i)
    for i in speeds:
        queue2.append(i)
    while queue1:
        sum = 0
        while queue1 and queue1[0] >= 100:
            queue1.popleft()
            queue2.popleft()
            sum += 1
        if sum != 0:
            answer.append(sum)
        sum = 0
       
        for i in range(len(queue1)):
            if queue1[i] < 100:
                queue1[i] += queue2[i]
    return answer