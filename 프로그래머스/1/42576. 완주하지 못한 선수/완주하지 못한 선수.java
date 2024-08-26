import java.util.*;

class Solution {
    
    static String answer = "";
    
    public String solution(String[] participant, String[] completion) {
        
        HashMap<String, Integer> set = new HashMap<>();
        
        for (String part : participant ){
            set.put(part, set.getOrDefault(part, 0) + 1);
        }
        
        for (String comp : completion) {
            set.put(comp, set.get(comp) - 1);
        }
        
        for (String one : set.keySet()){
            if(set.get(one) > 0){
                return one;
            }
        }
        return answer;
    }
}