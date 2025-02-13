import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb =  new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        int[][] map = new int[101][101];

        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                map[i][j] = 0;
            }
        }

        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for (int i = x; i < x + 10; i++) {
                for (int j = y; j < y + 10; j++) {
                    map[i][j] = 1;
                }
            }
        }

        int cnt = 0;

        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if(map[i][j] == 1) cnt++;
            }
        }

        System.out.println(cnt);
    }
}
