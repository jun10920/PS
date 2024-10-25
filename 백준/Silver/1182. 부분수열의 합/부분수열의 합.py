from itertools import combinations
n, s = map(int, input().split())
numList = list(map(int, input().split()))
count = 0

def dfs(s):
    global count
    for i in range(1, n + 1):
        for j in combinations(numList, i):
            if sum(j) == s:
                count += 1
    print(count)
dfs(s)