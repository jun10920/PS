def solution(N, number):
    if N == number:
        return 1
    
    # dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # 'N', 'NN', 'NNN'...

    for i in range(1, 9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            return i
    
    return -1
