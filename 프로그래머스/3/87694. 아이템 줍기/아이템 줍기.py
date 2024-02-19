from collections import deque

def bfs(board, start_x, start_y, end_x, end_y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
    board[start_x][start_y] = -1  # 시작점 방문 표시

    while queue:
        x, y, distance = queue.popleft()
        if (x, y) == (end_x, end_y):
            return distance // 2  # 확장된 지도에서의 거리를 반으로 줄임

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if board[nx][ny] == 1:
                board[nx][ny] = -1  # 방문 표시
                queue.append((nx, ny, distance + 1))
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]  # 지도 확장

    # 경계선 그리기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2  # 좌표 확장
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부 경계선
                    board[i][j] = -1
                elif board[i][j] != -1:  # 외부 경계선
                    board[i][j] = 1

    # BFS를 사용하여 최단 거리 계산
    return bfs(board, characterX * 2, characterY * 2, itemX * 2, itemY * 2)
