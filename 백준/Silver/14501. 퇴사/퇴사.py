n = int(input())

tempList = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(count, profit, restCount):
    global answer
    if count == n:
        answer = max(profit, answer)
        return
    if restCount > 0:
        dfs(count + 1, profit, restCount - 1)
    else:
        rest, tempProfit = tempList[count]

        dfs(count + 1, profit, restCount)
        if count + rest <= n:
            dfs(count + 1, profit + tempProfit, rest - 1)

dfs(0, 0, 0)

print(answer)