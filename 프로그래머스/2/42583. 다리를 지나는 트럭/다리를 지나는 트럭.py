from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리를 0으로 초기화
    current_weight = 0
    
    while truck_weights or current_weight:  # 대기 트럭이 있거나 다리 위에 트럭이 있는 동안
        time += 1
        current_weight -= bridge.popleft()  # 다리에서 트럭 하나가 나가면서 무게 감소
        
        if truck_weights:  # 대기 트럭이 있는 경우
            if current_weight + truck_weights[0] <= weight:  # 다음 트럭이 다리에 올라올 수 있는 경우
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:  # 다음 트럭이 다리에 올라올 수 없는 경우
                bridge.append(0)
    
    return time