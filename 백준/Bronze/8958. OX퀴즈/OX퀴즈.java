

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            String sen = br.readLine().trim();
            int score = 0;
            int current = 1;

            for (int j = 0; j < sen.length(); j++) {
                if (sen.charAt(j) == 'O') {
                    score += (current++);
                } else {
                    current = 1;
                }
            }
            sb.append(score).append("\n");
        }
        System.out.println(sb);
    }
}

