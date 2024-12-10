from collections import Counter

n = int(input())
li = []

minNum = float("inf")
maxNum = float("-inf")
for _ in range(n):
    num = int(input())
    li.append(num)

    minNum = min(minNum, num)
    maxNum = max(maxNum, num)

av = round(sum(li) / n)
li.sort()
mid = li[int(n / 2)]
count = Counter(li)

maxCount = max(count.values())
maxCountLi = []
for i in count.items():
    v, c = i
    if c == maxCount:
        maxCountLi.append(v)

print(av)
print(mid)

if len(maxCountLi) > 1:
    maxCountLi.sort()

    print(maxCountLi[1])
else:
    print(maxCountLi[0])


r = abs(maxNum - minNum)
print(r)
