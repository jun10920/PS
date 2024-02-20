from collections import deque

def dfs(computers, visited, start):
    queue = deque([start])
    
    while queue:
        j = queue.popleft()
        if not visited[j]:
            visited[j] = True
            for i in range(len(computers)):
                if computers[j][i] == 1 and not visited[i]:
                    queue.append(i)

def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for start in range(n):
        if not visited[start]:
            dfs(computers, visited, start)
            count += 1
    return count