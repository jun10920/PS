from itertools import product

def solution(numbers, target):
    
    list1 = [(i, -i) for i in numbers]
    candidate = list(map(sum, product(*list1)))
    return candidate.count(target)