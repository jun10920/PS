

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String sen = br.readLine();
            int score = 0;
            int current = 0;

            for (int j = 0; j < sen.length(); j++) {
                if (sen.charAt(j) == 'O') {
                    current++;
                    score += current;
                } else {
                    current = 0;
                }
            }

            System.out.println(score);
        }

    }
}