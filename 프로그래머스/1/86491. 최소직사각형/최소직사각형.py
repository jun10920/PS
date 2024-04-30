def solution(sizes):
    
    max1 = 0
    max2 = 0
    
    for i in sizes:
        i.sort(reverse = True)
        
        if i[0] > max1:
            max1 = i[0]
        if i[1] > max2:
            max2 = i[1]
    
    return max1 * max2