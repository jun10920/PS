def solution(nums):
    first = len(nums) // 2
    nums = set(nums)
    second = len(nums)
    
    return first if first < second else second 
