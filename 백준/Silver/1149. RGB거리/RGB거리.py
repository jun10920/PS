n = int(input())
answer = float("inf")
pointList = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * 3 for _ in range(n)]

def dfs(count, now):
    global answer
    if count == n:
        return 0
    if dp[count][now] != -1:
        return dp[count][now]

    ret = float('inf')

    for i in range(3):
        if i == now:
            continue
        ret = min(ret, dfs(count + 1, i) + pointList[count][i])

    dp[count][now] = ret
    return dp[count][now]

for i in range(3):
    answer= min(dfs(0, i), answer)

print(answer)