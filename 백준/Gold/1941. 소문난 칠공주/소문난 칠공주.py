from collections import deque
from itertools import combinations

count = 0
maps = [input() for _ in range(5)]
maps2 = []
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(li):
    idxli = set(i[0] for i in li)

    # idxli에서 튜플 하나를 꺼내 queue에 추가
    start = idxli.pop()  # idxli에서 하나 꺼내기
    queue = deque([start])  # 튜플 형태로 deque 초기화
    temp = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if (ny, nx) in idxli:
                queue.append((ny, nx))
                idxli.remove((ny, nx))  # 튜플 형태로 제거
                temp += 1

    return temp == 7


for i in range(5):
    for j in range(5):
        maps2.append(((i, j), maps[i][j]))

for i in list(combinations(maps2, 7)):
    sCount = 0
    for j in i:
        if j[1] == 'S':
            sCount += 1

    if sCount >= 4:
        if bfs(i):
            count += 1

print(count)