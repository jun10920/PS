from collections import defaultdict

def dfs(network, wire, visited):
    visited.add(wire)
    
    count = 1
    for i in network[wire]:
        if i not in visited:
            count += dfs(network, i, visited)
    return count
    

def solution(n, wires):
    network = defaultdict(list)
    
    for i in range(len(wires)):
        network[wires[i][0]].append(wires[i][1]) 
        network[wires[i][1]].append(wires[i][0]) 
    
    min_diff = n
    
    for i in range(len(wires)):
        network[wires[i][0]].remove(wires[i][1]) 
        network[wires[i][1]].remove(wires[i][0])
        
        visited = set()
        
        count = dfs(network, wires[i][0], visited)
        diff = abs(count - (n - count))
        
        min_diff = min(diff, min_diff)
        
        network[wires[i][0]].append(wires[i][1]) 
        network[wires[i][1]].append(wires[i][0]) 
        
    return min_diff