from itertools import combinations

n, s = map(int, input().split())
numList = list(map(int, input().split()))

count = 0

# 부분 수열의 길이를 1부터 n까지 순회
for i in range(1, n + 1):
    # 길이가 i인 모든 조합을 생성
    for comb in combinations(numList, i):
        if sum(comb) == s:
            count += 1

# 결과 출력
print(count)