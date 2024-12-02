n, k = map(int, input().split())
nLi = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * k for _ in range(n)]
answer = float("-inf")

def dfs(count, total_w):
    global answer

    if total_w >= k:
        return 0

    if count == n:
        return 0

    if dp[count][total_w] != -1:
        return dp[count][total_w]

    cur_w, cur_v = nLi[count][0], nLi[count][1]

    ret = float("-inf")

    if total_w + cur_w <= k:
        ret = max(ret, dfs(count + 1, total_w + cur_w) + cur_v)

    ret = max(ret, dfs(count + 1, total_w))

    dp[count][total_w] = ret

    return dp[count][total_w]

dfs(0, 0)
print(dp[0][0])