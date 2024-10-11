def dfs(numbers, target, index, current):
    if index == len(numbers):
        return 1 if current == target else 0
    else:
        return dfs(numbers, target, index + 1, current + numbers[index]) +dfs(numbers, target, index + 1, current - numbers[index])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)