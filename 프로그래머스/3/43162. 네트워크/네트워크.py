def dfs(computers, visited, start):
    stack = [start]
    
    while stack:
        j = stack.pop()
        if not visited[j]:
            visited[j] = True
            for i in range(len(computers)):
                if computers[j][i] == 1 and not visited[i]:
                    stack.append(i)

def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    for start in range(n):
        if not visited[start]:
            dfs(computers, visited, start)
            network_count += 1
            
    return network_count
