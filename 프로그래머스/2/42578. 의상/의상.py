from collections import defaultdict
from functools import reduce

def solution(clothes):
    arr = defaultdict(list)
    for i in clothes:
        arr[i[1]] = arr.get(i[1], 0) + 1
     
    answer = 1
    for i in arr.values():
        answer *= i + 1
    
    return answer -1