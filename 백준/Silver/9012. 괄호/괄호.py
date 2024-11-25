n = int(input())
while n:
    temp = input()
    answer = 'YES'
    if temp == ".":
        break
    li = []
    for i in temp:
        if i == '(':
            li.append(i)
        if i == ')':
            if li and li[-1] == '(':
                li.pop()
            else:
                answer = 'NO'
                break
        if i == '[':
            li.append(i)
        if i == ']':
            if li and li[-1] == '[':
                li.pop()
            else:
                answer = 'NO'
                break

    if len(li) == 0 and answer == 'YES':
        print(answer)
    else:
        answer = 'NO'
        print(answer)
    n -= 1