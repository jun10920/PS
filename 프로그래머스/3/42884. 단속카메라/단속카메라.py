def solution(routes):
    
    routes.sort(key = lambda x : x[1])
    answer = 1
    current = routes[0][1]
    print(routes)

    
    for i in routes[1:]:
        if current < i[0]:
            answer += 1
            current = i[1]
            
    return answer