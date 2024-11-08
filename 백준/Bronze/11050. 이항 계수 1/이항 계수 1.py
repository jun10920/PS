n, k = map(int, input().split())
lis = [i for i in range(n)]

dp = {}

def dfs(count, selected_count):
    global answer

    if selected_count== k:
        return 1

    if count == n:
        return 0

    if (count, selected_count) in dp:
        return dp[(count, selected_count)]

    result = dfs(count + 1, selected_count + 1) + dfs(count + 1, selected_count)
    dp[(count, selected_count)] = result

    return result

print(dfs(0, 0))