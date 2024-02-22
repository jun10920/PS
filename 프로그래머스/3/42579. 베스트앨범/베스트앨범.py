from collections import defaultdict
def solution(genres, plays):
    
    arr1 = defaultdict(int)
    arr2 = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        arr1[g] = arr1.get(g, 0) + p
        arr2[g].append((p, i))
        
    sgenre = sorted(arr1, key = arr1.get, reverse = True)
    
    answer = []
    for i in sgenre:
        answer += sorted(arr2[i], key = lambda x: (-x[0], x[1]))[:2]
    answer = list(map(lambda x: x[1], answer))
    return answer