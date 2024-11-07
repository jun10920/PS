n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
def dfs(count):

    if count == m:
        print(*selected)
        return

    for i in range(n):
        selected[count] = numList[i]
        dfs(count + 1)

selected = [0] * m
dfs(0)