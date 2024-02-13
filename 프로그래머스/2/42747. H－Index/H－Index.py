def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    
    for i, v in enumerate(citations):
        if v >= i + 1:
            answer = i + 1
        else:
            break

    return answer