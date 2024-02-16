from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    arr1 = defaultdict(int)
    arr2 = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        arr1[g] += p
        arr2[g].append((i,p)) 
        
    arr1 = sorted(arr1, key= arr1.get, reverse=True)
    print(arr2)
    for g in arr1:
        sorted_songs= sorted(arr2[g], key = lambda x: (-x[1], x[0]))
        answer += [s[0] for s in sorted_songs[:2]]
    print(answer)
    
    return answer