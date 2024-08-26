import java.util.*;

class Solution {
    
    static int answer = 1;
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> set = new HashMap<>();
        
        for (String[] c : clothes) {
            set.put(c[1], set.getOrDefault(c[1], 0) + 1);
        }
        
        for (int count : set.values()){
            answer *= (count + 1);
        }
        
        return answer - 1;
    }
}