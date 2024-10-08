from collections import defaultdict

def dfs(graph, node, visited):
    visited.add(node)
    count = 1
    
    for i in graph[node]:
        if i not in visited:
            count += dfs(graph, i, visited)
    
    return count
    

def solution(n, wires):
    
    graph = defaultdict(list)
    
    for i in wires:
        v1, v2 = i
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = n
    
    for i in wires:
        v1, v2 = i
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = set()
        count = dfs(graph, v1, visited)
        
        diff = abs(count - (n-count))
        min_diff = min(diff, min_diff)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return min_diff