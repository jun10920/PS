def solution(number, k):
    
    stack = [number[0]]

    for i in number[1:]:
        while k != 0 and stack and int(i) > int(stack[-1]):
            stack.pop()
            k -= 1
        stack.append(i)
            
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack) 