n, s = map(int, input().split())
numList = list(map(int, input().split()))

count = 0

def dfs(index, current_sum):
    global count
    
    # 모든 요소를 다 탐색한 경우
    if index == n:
        # 부분 수열의 합이 s와 같을 때만 카운트 증가 (빈 수열 제외)
        if current_sum == s:
            count += 1
        return
    
    # 현재 인덱스의 숫자를 포함하지 않는 경우
    dfs(index + 1, current_sum)
    
    # 현재 인덱스의 숫자를 포함하는 경우
    dfs(index + 1, current_sum + numList[index])

# DFS 탐색 시작
dfs(0, 0)

# s가 0일 때는 빈 수열을 제외해야 하므로 count에서 1을 뺀다
if s == 0:
    count -= 1

print(count)
