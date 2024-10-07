from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    count = 0
    
    while truck_weights or current_weight != 0:
        temp = bridge.popleft()
        current_weight -= temp
        count += 1
        
        if truck_weights and truck_weights[0] + current_weight <= weight:
            truck = truck_weights.popleft()
            current_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)
    
    return count