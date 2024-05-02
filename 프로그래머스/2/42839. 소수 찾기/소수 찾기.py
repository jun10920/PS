from itertools import permutations

def check(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**(1/2) + 1)):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    count = 0
    arr = []
    for i in range(1, len(numbers) + 1):
        arr += [i for i in permutations(numbers, i)]
    
    num = [int(''.join(t)) for t in arr]
    
    result = set()
    for i in num:
        if check(i):
            result.add(i)
            
    
    return len(result)