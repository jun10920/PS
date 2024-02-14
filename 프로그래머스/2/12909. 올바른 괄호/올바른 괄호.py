def solution(s):
    answer = True
    if s[0] == ')' or s[-1] == '(':
        return False
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack