function solution(nums) {
    
    const unique = new Set(nums);
    const temp = nums.length / 2;
    
    return Math.min(unique.size, temp);
}