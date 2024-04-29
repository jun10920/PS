def solution(citations):
    citations.sort(reverse=True)
    
    for i, v in enumerate(citations):
        if i >= v:
            return i 
    return len(citations)

def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # H-Index 찾기
    h_index = 0
    for i, citation in enumerate(citations):
        # 인용 횟수가 논문 수(인덱스+1)보다 크거나 같은 경우, H-Index 후보로 간주
        if citation >= i + 1:
            h_index = i + 1
        else:
            # 나머지 논문은 h번 이하 인용되었으므로 반복 중지
            break
    
    return h_index