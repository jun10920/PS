from collections import defaultdict

def solution(tickets):
    
    routes = defaultdict(list)
    
    for start, end in tickets:
        routes[start].append(end)
        
    for start in routes:
        routes[start].sort()
        
    stack = ['ICN']
    path = []
    
    while stack:
        top = stack[-1]
        
        if routes[top]:
            stack.append(routes[top].pop(0))
        else:
            path.append(stack.pop())
            
    return path[::-1]
