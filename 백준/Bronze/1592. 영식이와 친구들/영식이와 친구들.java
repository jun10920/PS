import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[n];
        int cur = 0;
        arr[cur] = 1; 
        int ans = 0;
        
        while (true) {
            if (arr[cur] == m) break;
            
            if (arr[cur] % 2 != 0) { 
                cur = (cur + l) % n;
            } else {  
                cur = (cur - l + n) % n;
            }
            
            ans++;
            arr[cur]++;
            
            if (arr[cur] == m) break;
        }
        
        System.out.println(ans);
    }
}
