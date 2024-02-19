def solution(bridge_length, weight, truck_weights):
    
    current_weight = 0
    count = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while current_weight != 0 or truck_weights:
        count += 1
        current_weight -= bridge.pop(0)
        
        if truck_weights and current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
    return count