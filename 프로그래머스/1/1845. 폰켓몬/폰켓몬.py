def solution(nums):
    howMany = len(nums)//2
    return min(howMany, len(set(nums)))
