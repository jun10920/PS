from collections import deque

def solution(p, location):
    
    # 우선순위와 인덱스를 함께 저장하는 큐
    # count : 순서
    # 0번 인덱스 popleft()
    # 순회하면서 가장 우선순위가 높으면 
        # count += 1
        # 인덱스도 location이랑 같으면 return count
    # 우선순위가 더 큰 게 있으면 append()
        # count +1
    
    tempList = [(v, i) for i, v in enumerate(p)]
    queue = deque(tempList)
    count = 0
    
    while queue:
        temp = queue.popleft()

        if any(temp[0] < item[0] for item in queue):
            queue.append(temp)
        else:
            count += 1
            if temp[1] == location:
                return count
        
#         if temp[0] < max(queue, key=lambda x: x[0])[0]:
#             queue.append(temp)
#             continue
        
#         count += 1
#         if temp[1] == location:
#             return count