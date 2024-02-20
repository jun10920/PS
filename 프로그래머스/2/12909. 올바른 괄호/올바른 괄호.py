def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
    