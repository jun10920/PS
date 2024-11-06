n = int(input())
tasteList = []

for _ in range(n):
    sin, ssn = map(int, input().split())
    tasteList.append((sin, ssn))

answer = float('inf')

def dfs(count, tempTaste, use):
    global answer
    if count == n and use > 0:
        answer = min(answer, abs(tempTaste[0] - tempTaste[1]))
        return
    elif count == n:
        return

    newSin, newSsn = tasteList[count]
    sin, ssn = tempTaste

    dfs(count + 1, (sin, ssn), use)
    dfs(count + 1, (sin * newSin, ssn + newSsn), use +1)

dfs(0, (1, 0), 0)

print(answer)