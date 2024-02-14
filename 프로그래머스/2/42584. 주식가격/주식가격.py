def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = []
    
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = length - 1 - j
    
    return answer