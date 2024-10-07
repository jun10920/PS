import heapq

def solution(s, K):
    
    cnt = 0
    heapq.heapify(s)
    
    while s[0] < K:
        
        if len(s) < 2:
            return -1
        
        temp1 = heapq.heappop(s)
        temp2 = heapq.heappop(s)
        heapq.heappush(s, temp1 + (temp2 * 2))
        cnt += 1
    
    return cnt