from itertools import product

def solution(word):
    
    temp = ['A', 'E', 'I', 'O', 'U']
    senList = []
    
    for i in range(1, 6):
        for j in product(temp, repeat = i):
            senList.append(''.join(j))
    
        
    senList.sort()

    return senList.index(word) + 1