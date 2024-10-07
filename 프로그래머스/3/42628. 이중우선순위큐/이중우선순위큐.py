import heapq

def solution(operations):
    heap = []  # 최소 힙

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == "I":
            heapq.heappush(heap, value)
        elif heap:
            if value == 1:
                heap.remove(max(heap))  # 최댓값 삭제
            else:
                heapq.heappop(heap)  # 최솟값 삭제

            # 힙 속성 복구
            heapq.heapify(heap)

    if not heap:
        return [0, 0]
    else:
        return [max(heap), heap[0]]  # 최댓값, 최솟값 반환