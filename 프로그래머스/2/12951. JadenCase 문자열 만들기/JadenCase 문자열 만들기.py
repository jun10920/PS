def solution(s):
    
    words = s.split(' ')
    result = []
    
    for i in words:
        if i:
            result.append(i[0].upper() + i[1:].lower())
        else:
            result.append('')

    return ' '.join(result)