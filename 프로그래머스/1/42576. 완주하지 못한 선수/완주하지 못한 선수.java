import java.util.*;
import java.io.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. HashMap을 이용해 각 이름의 등장 횟수를 기록
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String player : participant) {
            map.put(player, map.getOrDefault(player, 0) + 1);
        }
        
        // 2. completion 리스트를 돌며 map에서 해당 이름의 횟수를 차감
        for (String player : completion) {
            map.put(player, map.get(player) - 1);
        }
        
        // 3. map에서 값이 1인 참가자를 찾음 (완주하지 못한 참가자)
        for (String key : map.keySet()) {
            if (map.get(key) == 1) {
                return key;
            }
        }
        
        // 예외 처리 (문제상 발생하지 않음)
        return "";
    }
}