import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    sync = {}  # 동기화를 위한 딕셔너리

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            sync[value] = sync.get(value, 0) + 1
        elif value == -1 and min_heap:  # 최솟값 삭제
            while min_heap and sync[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            if min_heap:
                sync[min_heap[0]] -= 1
                heapq.heappop(min_heap)
        elif value == 1 and max_heap:  # 최댓값 삭제
            while max_heap and sync[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            if max_heap:
                sync[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

    # 동기화
    while min_heap and sync[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and sync[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]
