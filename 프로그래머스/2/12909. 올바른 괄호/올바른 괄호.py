def solution(s):
    
    if s[0] == ')' or s[-1] == '(':
        return False
    
    list1 = []
    
    for i in s:
        if i == "(":
            list1.append(i)
        else:
            if not list1:
                return False
            else:
                list1.pop()
    
    if list1:
        return False
    else:
        return True