from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 모든 트럭이 다리를 건너는데 걸리는 최소 시간
    # bridge_length 다리 길이
    # weight 최대 무게
    # truck_weights 대기 트럭 리스트

    # 대기 트럭 리스트가 비고, bridge의 총 무게가 0이 될 때까지
    # 매번 다리 위의 트럭 리스트의 key() 값의 합이 다리 위의 총 무게 보다 적으면
        # 현재 대기 트럭 리스트에서 하나를 다리 위의 트럭 리스트에 넣음
        # count += 1
    # 매번 다리 위의 트럭 리스트의 value() 값 중에 bridge_length보다 커지면
        # 다리 위의 트럭리스트에서 제거 (0으로 처리)
    
    truckList = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    currentW = 0
    count = 0
    
    while truckList or currentW > 0:
        count += 1
        currentW -= bridge.popleft()
        
        if truckList:
            if truckList[0] + currentW <= weight:
                temp = truckList.popleft()
                currentW += temp
                bridge.append(temp)
            else:
                bridge.append(0)

    return count