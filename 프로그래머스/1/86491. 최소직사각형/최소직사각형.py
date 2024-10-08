def solution(sizes):
    
    temp1 = []
    temp2 = []
    for i in sizes:
        i.sort(reverse = True)
        
        temp1.append(i[0])
        temp2.append(i[1])

    return max(temp1) * max(temp2)