def solution(nums):
    
    nums1 = set(nums)
    return min(len(nums1), int(len(nums) / 2))