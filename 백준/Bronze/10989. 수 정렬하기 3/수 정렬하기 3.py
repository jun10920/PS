n = int(input())

counts = [0] * 100001

for _ in range(n):
    number = int(input())
    counts[number] += 1

for i in range(1, 10001):
    if counts[i] > 0:
        for _ in range(counts[i]):
            print(i)