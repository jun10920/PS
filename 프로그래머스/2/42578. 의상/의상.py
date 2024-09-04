from collections import defaultdict

def solution(clothes):
    
    temp = defaultdict(int)
    answer = 1
    
    for i in clothes:
        temp[i[1]] += 1
    
    
    for i in temp.values():
        answer *= (i+1)        
    
    return answer - 1