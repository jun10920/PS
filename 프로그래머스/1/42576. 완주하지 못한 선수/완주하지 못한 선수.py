from collections import defaultdict

def solution(part, comp):
    
    temp = defaultdict(int)
    
    for i in part:
        temp[i] += 1
        
    for i in comp:
        temp[i] -= 1
    
    for i in temp.items():
        if i[1] == 1:
            return i[0]