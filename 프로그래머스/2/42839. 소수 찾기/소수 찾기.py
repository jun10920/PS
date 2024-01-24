from itertools import permutations

def checkPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    temp = [int(i) for i in numbers]

    for j in range(1, len(temp) + 1):
        perms = list(permutations(temp, j))
        for perm in perms:
            num = int(''.join(map(str, perm)))
            if checkPrime(num):
                answer.add(num)

    return len(answer)