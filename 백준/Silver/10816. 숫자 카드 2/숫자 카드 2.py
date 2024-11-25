from collections import defaultdict

li = defaultdict(int)

n = int(input())
nLi = list(map(int, input().split()))
for i in nLi:
    li[i] = li.get(i, 0) + 1

m = int(input())
mLi = list(map(int, input().split()))

for i in mLi:
    print(li[i], end = ' ')