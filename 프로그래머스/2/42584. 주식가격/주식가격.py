def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
                
        answer[i] = count
    
    
    return answer