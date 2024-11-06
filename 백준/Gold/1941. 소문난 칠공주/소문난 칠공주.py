from itertools import combinations
from collections import deque

# 입력 받기
maps = [input().strip() for _ in range(5)]

# 상하좌우 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 총 경우의 수
count = 0

# 5x5 좌표를 리스트로 변환
positions = [(i, j) for i in range(5) for j in range(5)]

# 7명을 선택하는 모든 조합을 구함
for comb in combinations(positions, 7):
    # 'S'의 개수를 카운트
    s_count = sum(1 for y, x in comb if maps[y][x] == 'S')
    
    # 'S'가 4명 미만이면 조건 불충족
    if s_count < 4:
        continue
    
    # 선택된 7명이 연결되어 있는지 확인 (BFS)
    queue = deque([comb[0]])
    visited = {comb[0]}
    connected_count = 1
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (ny, nx) in comb and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx))
                connected_count += 1
                
    # 7명이 모두 연결되어 있으면 경우의 수 증가
    if connected_count == 7:
        count += 1

print(count)
