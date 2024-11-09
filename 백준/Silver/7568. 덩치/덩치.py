n = int(input())
li = []

for _ in range(n):
    weight, height = map(int, input().split())
    li.append((weight, height))

ranks = [1] * n  

for i in range(n):
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            ranks[i] += 1

for rank in ranks:
    print(rank, end=' ')