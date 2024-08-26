import java.util.*;
import java.io.*;

class Solution {
    
    static int answer = 5000;
    
    public int solution(int[] nums) {
        
        int numLen = nums.length / 2;
        HashSet<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            set.add(num);
        }
        
        answer = Math.min(set.size(), numLen);
        
        return answer;
    }
}