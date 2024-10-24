n, s = map(int, input().split(" "))
numList = [i for i in list(map(int, input().split(" ")))]
count = 0
visited = [False] * len(numList)

def dfs(idx, current_sum):
    global count
    if idx == n:
        if current_sum == s:
            count += 1
        return
    dfs(idx + 1, current_sum + numList[idx])
    dfs(idx + 1, current_sum)

if s == 0:
    count -= 1

dfs(0, 0)
print(count)
