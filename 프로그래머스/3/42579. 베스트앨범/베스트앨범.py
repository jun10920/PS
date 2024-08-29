from collections import defaultdict

def solution(g, p):
    # 장르가 높은 순
    # 장르 내에서 많이 재생된 순
    # 재생 횟수가 같다면 고유 번호가 낮은 순
    # 각 장르 별로 최대 2개
    
    # dict 2개 (장르, 재생 회수 합) / (장르, (재생회수, 고유 번호))
    # 1번 dict 정렬 - 재생 회수 합이 높은 순으로
    # 1번 dict의 key 순으로 2번 dict의 장르의 재생회수, 고유 번호 순으로 정렬
    # 2번 dict의 각 장르의 고유번호를 answer에 기입
    answer = []
    dict1 = defaultdict(int)
    dict2 = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(g, p)):
        dict1[g] += p
        dict2[g].append((p, i))
    
    sorted_g = sorted(dict1.keys(), key = lambda x : dict1[x], reverse = True)
        
    for i in sorted_g:
        
        sorted_s = sorted(dict2[i], key = lambda x : (-x[0], x[1]))
        
        answer += [song[1] for song in sorted_s[:2]]
    return answer