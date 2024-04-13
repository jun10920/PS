from collections import deque

def solution(p, l):
    
    list = deque()
    count = 0
    
    for i, v in enumerate(p):
        list.append((v,i))   
    
    while list:
        i = list.popleft()
        if any(i[0] < other[0] for other in list):
            list.append(i)
        else:
            count += 1
            
            if i[1] == l:
                return count