import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        command, value = i.split()
        value = int(value)
        
        if command == 'I':
            heapq.heappush(heap, value)
        elif heap:
            if value == -1:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
        heapq.heapify(heap)
        
    if not heap:
        return [0, 0]
    else:
        return [max(heap), heap[0]] 