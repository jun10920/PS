from collections import deque

def solution(length, weight, tw):
    
    count, cw = 0, 0
    # bridge 생성
    bridge = deque([0 for _ in range(length)])
    # tw랑 bridge queue로 생성
    tw = deque(tw)
    # cw가 0이 아니고 or tw가 남아있다면
    while cw != 0 or tw:
        count += 1
        cw -= bridge.popleft()
        
        if tw and cw + tw[0] <= weight:
            truck = tw.popleft()
            bridge.append(truck)
            cw += truck
        else:
            bridge.append(0)
    return count