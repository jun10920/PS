from collections import deque
n, k = map(int, input().split())

numLi = deque([i + 1 for i in range(n)])

answer = []

while numLi:
    temp = k - 1

    while temp > 0:
        numLi.append(numLi.popleft())
        temp -=1

    answer.append(numLi.popleft())

print("<" + ", ".join(map(str, answer)) + ">")    