
from itertools import combinations
from collections import deque

def spread_virus(grid, virus_positions):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque(virus_positions)

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                queue.append((nx, ny))


def count_safe_area(grid):
    return sum(row.count(0) for row in grid)


def solve_lab():
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]
    empty_spaces = [(i, j) for i in range(len(lab)) for j in range(len(lab[0])) if lab[i][j] == 0]
    virus_positions = [(i, j) for i in range(len(lab)) for j in range(len(lab[0])) if lab[i][j] == 2]
    max_safe_area = 0

    for walls in combinations(empty_spaces, 3):
        temp_lab = [row[:] for row in lab]
        for x, y in walls:
            temp_lab[x][y] = 1
        spread_virus(temp_lab, virus_positions)
        max_safe_area = max(max_safe_area, count_safe_area(temp_lab))

    return max_safe_area


print(solve_lab())