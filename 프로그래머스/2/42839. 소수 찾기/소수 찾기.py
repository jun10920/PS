from itertools import permutations

def checkPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    
    temp = [i for i in numbers]
    temp2 = []
    
    for i in range(1, len(numbers) + 1):
        temp2 += list(permutations(temp, i))
    
    temp3 = set([int(''.join(i)) for i in temp2])
            
    answer = 0
    for i in temp3:
        if checkPrime(i):
            answer += 1
    return answer