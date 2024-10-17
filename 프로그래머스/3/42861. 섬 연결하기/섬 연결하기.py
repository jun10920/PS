import heapq

def solution(n, costs):

    graph = [[] for _ in range(n)]
    for u, v, cost in costs:
        graph[u].append((cost,v))
        graph[v].append((cost,u))
        
    visited = [False] * n # 노드 방문 여부
    min_heap = [(0, 0)] # (간선 가중치, 시작 노드), 0번 노드에서 시작
    total_cost = 0
    edges_used = 0
    
    while edges_used < n:
        cost, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += cost
        edges_used += 1
        
        for edge_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))
    
    return total_cost