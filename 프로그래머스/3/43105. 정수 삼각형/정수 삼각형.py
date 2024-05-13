def solution(triangle):
    # dp 배열 초기화
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for n in range(1, len(triangle)):
        for i in range(n + 1):
            if i > 0:
                dp[n][i] = max(dp[n][i], dp[n-1][i-1] + triangle[n][i])
            if i < n:
                dp[n][i] = max(dp[n][i], dp[n-1][i] + triangle[n][i])
    
    return max(dp[-1])

# 이제 이 함수는 각 층을 거치면서 가능한 최대 합을 계산하고, 마지막 층에서의 최대값을 반환합니다.
