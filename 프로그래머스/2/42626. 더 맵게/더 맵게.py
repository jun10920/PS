import heapq

def solution(s, k):
    h = heapq
    h.heapify(s)
    count = 0

    while s[0] < k:
        if len(s) < 2:
            return -1
        first = h.heappop(s)
        second = h.heappop(s)
        new = first + (second * 2)
        h.heappush(s, new)
        count +=1
    return count