def solution(number, k):
    stack = [int(number[0])]
    
    for i in number[1:]:
        while k != 0 and stack and stack[-1] < int(i):
            stack.pop()
            k -= 1
        stack.append(int(i))
    
    if k != 0:
        stack = stack[:-k]
    stack = list(map(str, stack))
    return ''.join(stack)