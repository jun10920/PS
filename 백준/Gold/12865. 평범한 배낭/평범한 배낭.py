n, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (k + 1) for _ in range(n)]

def dfs(count, curK):
    if count == n:
        return 0

    if dp[count][curK] != -1:
        return dp[count][curK]

    ret = float("-inf")

    if curK + li[count][0] <= k:
        ret = max(ret, dfs(count + 1, curK + li[count][0]) + li[count][1])

    ret = max(ret, dfs(count + 1, curK))

    dp[count][curK] = ret
    return dp[count][curK]


print(dfs(0, 0))