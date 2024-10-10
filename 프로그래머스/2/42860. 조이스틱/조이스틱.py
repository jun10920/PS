def solution(name):
    col = 0
    for i in name:
        tempCol = min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
        col += tempCol
    
    aInx = 0
    row = len(name) - 1
    for i, v in enumerate(name):
        if v == 'A':
            aInx = i
            while aInx < len(name) and name[aInx] == 'A':
                aInx += 1
            left = (0 if i == 0 else i - 1)
            right = len(name) - aInx
            row = min(row, left + right + min(left, right))

    return col + row