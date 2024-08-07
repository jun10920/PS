import heapq

def solution(s, k):
    
    heapq.heapify(s)
    count = 0
        
    while k > s[0]:
        if len(s) < 2:
            return -1
        
        first = heapq.heappop(s)
        second = heapq.heappop(s)
        new = first + (second * 2)
        heapq.heappush(s, new)
        count += 1

    return count