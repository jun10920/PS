import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        score = first + (second * 2)
        heapq.heappush(scoville, score)
        count += 1
    return count