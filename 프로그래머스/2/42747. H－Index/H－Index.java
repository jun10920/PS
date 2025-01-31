import java.util.*;

class Solution {
    public int solution(int[] citations) {
        
        int n = citations.length;
        Integer[] arr = new Integer[n];

        for (int i = 0; i < n; i++) {
            arr[i] = citations[i];
        }
        
        Arrays.sort(arr, (a, b) -> b - a);

        System.out.println(Arrays.toString(arr));

        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] < i + 1) {
                return i;
            }
        }
        
        return citations.length;
    }
}