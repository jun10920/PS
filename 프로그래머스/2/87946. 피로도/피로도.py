from itertools import permutations
def solution(k, dun):
    arr = list(permutations(dun, len(dun)))
    count= 0
    for i in arr:
        hp = k
        countImpl = 0
        for j in i:
            if hp >= j[0]:
                hp -= j[1]
                countImpl += 1
            count = max(count, countImpl)
    return count