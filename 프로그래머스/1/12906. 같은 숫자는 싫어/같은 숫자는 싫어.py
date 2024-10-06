def solution(arr):
    answer = []
    
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer