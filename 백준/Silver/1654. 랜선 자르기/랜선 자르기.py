import sys

input = sys.stdin.readline
k, n = map(int, input().split())
numLi = [int(input()) for _ in range(k)]

# 이진 탐색 범위 설정
low, high = 1, max(numLi)
answer = 0

while low <= high:
    mid = (low + high) // 2  # 중간 길이
    
    # mid 길이로 랜선을 나눠서 만들 수 있는 랜선 개수 계산
    count = sum(num // mid for num in numLi)
    
    if count >= n:  # n개 이상 만들 수 있다면, 길이를 늘려본다
        answer = mid  # 가능한 길이를 저장
        low = mid + 1
    else:  # n개 미만이라면, 길이를 줄인다
        high = mid - 1

print(answer)
