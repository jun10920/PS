def solution(nums):
    temp = len(set(nums))
    return min(temp, len(nums)//2)