n, m = map(int, input().split())

def dfs(count):

    if count == m:
        print(*selected)
        return

    for i in range(n):
        if i in visited:
          continue
        selected[count] = i + 1

        visited.add(i)
        dfs(count + 1)
        visited.remove(i)

selected = [0] * m
visited = set()
dfs(0)