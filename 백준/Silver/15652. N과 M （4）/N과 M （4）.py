n, m = map(int, input().split())
numList = [i + 1 for i in range(n)]

def dfs(count):
    if count == m:
        print(*selected)
        return

    for i in range(1, n + 1):
        if count > 0:
            if selected[count - 1] > i:
                continue
        selected[count] = i
        dfs(count + 1)

selected = [0] * m
dfs(0)