import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        
        List<Integer> li = new ArrayList<>();
        for (int num : numbers) {
            li.add(num);
        }
        
        Collections.sort(li, (a, b) -> (String.valueOf(b) + a).compareTo(String.valueOf(a) + b));
        
        if (li.get(0) == 0) {
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        for (int num : li) {
            sb.append(num);
        }
        
        return sb.toString();
    }
}