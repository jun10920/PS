from collections import deque

def solution(prior, location):
    
    pq = deque([])
    count = 0
    
    for i,v in enumerate(prior):
        pq.append([i,v])
            
    while pq:
        temp = pq.popleft()
        if pq and temp[1] < max(x[1] for x in pq):
            pq.append(temp)
        else:
            count +=1
            if location == temp[0]:
                return count