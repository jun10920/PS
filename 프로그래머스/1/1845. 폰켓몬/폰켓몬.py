def solution(nums):
    howMany = len(nums)//2
    
    arr = list(set(nums))
    result = len(arr) if len(arr) <= howMany else howMany
    print(result)
    return result