def solution(prices):
    length = len(prices)
    stack = []
    answer = [0] * length    
    
    for i in range(length):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        a = stack.pop()
        answer[a] = length - 1 - a
    return answer