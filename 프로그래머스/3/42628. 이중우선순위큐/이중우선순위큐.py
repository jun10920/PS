import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    sync = {}
    for i in operations:
        command, value = i.split()
        value = int(value)
        
        if command == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            sync[value] = sync.get(value, 0) + 1
        else:
            if value == -1 and min_heap:
                while min_heap and sync[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    sync[heapq.heappop(min_heap)] -= 1
            if value == 1 and max_heap:
                while max_heap and sync[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    sync[-heapq.heappop(max_heap)] -= 1
    while min_heap and sync[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and sync[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
        
    if not min_heap or not max_heap:
        return [0,0]
    else:
        return [-max_heap[0], min_heap[0]]