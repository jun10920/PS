def solution(triangle):
    
    # 각 층까지의 값을 저장하는 dp 배열 생성
    dp = [[] for _ in range(0,len(triangle))]
    maxNum = triangle[0][0]
    
    # 삼각형의 두 번째 층부터 시작하여 각 요소를 업데이트
    for n in range(1, len(triangle)):
        for i in range(n + 1):
            # 왼쪽 위에서 내려오는 경우
            if i > 0:
                dp[n][i] = max(dp[n][i], dp[n-1][i-1] + triangle[n][i])
            # 바로 위에서 내려오는 경우
            if i < n:
                dp[n][i] = max(dp[n][i], dp[n-1][i] + triangle[n][i])

    # 마지막 층의 최대값을 반환
    return max(dp[-1])