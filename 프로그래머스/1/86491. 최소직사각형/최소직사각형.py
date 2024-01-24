def solution(sizes):
    maxArr=[]
    minArr=[]
    for i in sizes:
        if i[0] > i[1]:
            maxArr.append(i[0])
            minArr.append(i[1])
        else:
            maxArr.append(i[1])
            minArr.append(i[0])
    return max(maxArr) * max(minArr)