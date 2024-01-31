from itertools import permutations

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    arr = []
    for i in range(1,len(numbers)+1):
        arr += list(permutations(numbers,i))
    
    arr2 = [int(''.join(t)) for t in arr]
    
    for i in arr2:
        if checkPrime(i):
            answer.add(i)
    
    return len(answer)