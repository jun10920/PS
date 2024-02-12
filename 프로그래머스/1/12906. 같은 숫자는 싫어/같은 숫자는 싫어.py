def solution(arr):
    stack = [arr[0]]
    for i in arr[1:]:
        while stack and stack[-1] == i:
            stack.pop()
        stack.append(i)
    return stack