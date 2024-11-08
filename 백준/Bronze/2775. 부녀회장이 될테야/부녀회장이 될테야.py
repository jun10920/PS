t = int(input())

# 1 5 15
# 1 4 10
# 1 3 6
# 1 2 3

apt = [[0] * 14 for _ in range(15)]

for i in range(14):
    apt[0][i] = (i + 1)

for i in range(1, 15):
    for j in range(14):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])