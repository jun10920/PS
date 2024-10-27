n = int(input())

cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
count = 0
def dfs(row):
    global count
    if row == n:
        count += 1

    for i in range(n):
        if not cols[i] and not diag1[i - row + (n - 1)] and not diag2[i + row]:
            cols[i] = diag1[i - row + (n - 1)] = diag2[i + row] = True
            dfs(row + 1)
            cols[i] = diag1[i - row + (n - 1)] = diag2[i + row] = False

    return count

print(dfs(0))