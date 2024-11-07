def solve():  
    N = int(input())  
    schedule = [[0, 0]]  
    for _ in range(N):  
        a, b = map(int, input().split())  
        schedule.append([a, b])  

    dp = [0] * (N+1)  
    for i in range(1, N+1):  
        day, pay = schedule[i]  
        day -= 1  
        # 상담이 완료되는 날짜에 받는 최대 비용 갱신해주기  
        if i + day <= N:  
            dp[i+day] = max(dp[i+day], dp[i-1] + pay)  
        # 오늘까지 벌 수 있는 최대 비용 갱신해주기  
        dp[i] = max(dp[i], dp[i-1])  
    print(dp[-1])  
solve()