from collections import deque
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    perm = list(permutations(dungeons, len(dungeons)))
    
    for i in perm:
        count = 0
        HP = k
        for j in range(0, len(dungeons)):
            minHP = i[j][0]
            minusHP = i[j][1]
            if minHP <= HP:
                HP -= minusHP
                count += 1
            else:
                break
        answer = max(answer, count)
        
    return answer