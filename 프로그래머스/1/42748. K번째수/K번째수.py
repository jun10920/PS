def solution(array, commands):
    
    answer = []
    
    for l in commands:
        i, j, k = l[0], l[1], l[2]
        
        arr = array[i - 1 : j]
        arr.sort()
        answer.append(arr[k-1])
        
    return answer