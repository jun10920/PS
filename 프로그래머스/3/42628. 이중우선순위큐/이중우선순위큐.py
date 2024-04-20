import heapq

def solution(operations):
    
    stack = []
    
    for i in operations:
        command, value = i.split()
        value = int(value)
        
        if command == 'I':
            heapq.heappush(stack, value)
        elif stack:
            if value == 1:
                stack.remove(max(stack))
            else:
                heapq.heappop(stack)
                
        heapq.heapify(stack)
            
    if stack:
        return [max(stack), stack[0]]
    else:
        return [0,0]