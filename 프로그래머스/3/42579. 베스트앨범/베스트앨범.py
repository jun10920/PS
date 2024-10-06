from collections import defaultdict

def solution(genres, plays):
    sorted_g = defaultdict(int)
    sorted_s = defaultdict(list)
    
    for g, (i, p) in zip(genres, enumerate(plays)):
        sorted_g[g] = sorted_g.get(g, 0) + p
        sorted_s[g].append([i, p])
        
    sorted_gl = sorted(sorted_g.keys(), key = sorted_g.get, reverse = True)
    
    answer = []
    
    for i in sorted_gl:
        sorted_sl = sorted(sorted_s[i], key = lambda x : (-x[1], x[0]))
        answer.extend([i[0] for i in sorted_sl][:2])
    
    return answer