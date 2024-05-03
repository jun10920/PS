from itertools import product

def solution(word):
    
    arr1 = ['A', 'E', 'I', 'O', 'U']
    arr2 = []
    
    for i in range(1, len(arr1) + 1):
        for combination in product(arr1, repeat = i):
            arr2.append(''.join(combination))
            
    arr2.sort()         
    answer = arr2.index(word) + 1
    
    return answer