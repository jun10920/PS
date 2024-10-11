from collections import deque

def bfs(computers, visited, start):
    
    queue = deque([start])
    
    while queue:
        temp = queue.popleft()
        visited[temp] = True
        for i in range(len(computers)):
            if computers[temp][i] == 1 and not visited[i]:
                queue.append(i)

def solution(n, computers):
    
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            count += 1
    return count