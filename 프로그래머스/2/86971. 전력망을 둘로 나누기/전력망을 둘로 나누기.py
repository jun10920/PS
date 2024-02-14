from collections import defaultdict, deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    count = 1  # 시작 노드를 포함하여 카운트 시작

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    # 그래프 초기화
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 최소 차이를 최대로 설정
    min_diff = n

    # 전선 순회 및 제거
    for v1, v2 in wires:
        # 전선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 송전탑 개수 계산
        count = bfs(graph, v1)

        # 송전탑 개수 차이 계산 및 최소 차이 업데이트
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)

        # 전선 복원
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_diff
