def solution(clothes):
    dic= {}
    for c, t in clothes:
        dic[t] = dic.get(t,0) + 1
    answer = 1
    for t in dic:
        answer *= (dic[t] + 1)
    return answer -1