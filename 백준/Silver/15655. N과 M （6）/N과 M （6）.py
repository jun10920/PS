n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
def dfs(count, visited):

    if count == m:
        print(*selected)
        return

    for i in range(n):
        if count > 0:
            if selected[count - 1] > numList[i]:
                continue
        if numList[i] not in visited:
            visited.add(numList[i])
            selected[count] = numList[i]
            dfs(count + 1, visited)
            visited.remove(numList[i])

selected = [0] * m
dfs(0, set())