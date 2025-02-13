import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb =  new StringBuilder();
        StringTokenizer st;

        Queue<Integer> li = new ArrayDeque<>();

        for (int i = 0; i < 10; i++) {
            int temp = Integer.parseInt(br.readLine());
            li.add(temp % 42);
        }

        int ans = 10;
        while (!li.isEmpty()) {
            int temp = li.poll();
            if (li.contains(temp)) {
                ans --;
            }
        }
        System.out.println(ans);
    }
}
