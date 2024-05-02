from itertools import permutations

def check(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(1/2)) + 1):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    arr = []
    
    for i in range(1, len(numbers) + 1):
        arr += list(set([i for i in permutations(numbers, i)]))
        
    num = [int(''.join(i)) for i in arr]
    result = set()
    for i in num:
        if check(i):
            result.add(i)

    return len(result)