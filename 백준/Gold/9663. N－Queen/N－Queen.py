n = int(input())

col = [False] * n
# 오른쪽 대각선 (\ 방향)
diag1 = [False] * (2 * n - 1)  # 행 - 열의 범위는 -(n - 1) ~ (n - 1)
# 왼쪽 대각선 (/ 방향)
diag2 = [False] * (2 * n - 1)  # 행 + 열의 범위는 0 ~ 2 * (n - 1)
count = 0

def backtrack(row):
    global count
    if row == n:
        count += 1
        return
    
    for i in range(n):
        if not col[i] and not diag1[row - i + (n - 1)] and not diag2[row + i]:
            col[i] = diag1[row - i + (n - 1)] = diag2[row + i] = True
            backtrack(row + 1)
            col[i] = diag1[row - i + (n - 1)] = diag2[row + i] = False

# 백트래킹 실행
backtrack(0)
print(count)