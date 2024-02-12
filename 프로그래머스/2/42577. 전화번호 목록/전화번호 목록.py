def solution(pb):
    answer = True
    pb.sort()
    for i in range(len(pb)- 1):
        if pb[i+1].startswith(pb[i]):
            answer = False
    return answer