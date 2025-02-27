import java.util.*;
import java.io.*;

public class Main {

    static int R;
    static int C;

    static char[][] map;

    static int[] dy = {-1, 0, 1};
    static int[] dx = {1, 1, 1};

    static int ans = 0;

    static boolean finished;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];

        for (int i = 0; i < R; i++) {
            char[] charArr = br.readLine().toCharArray();
            if (C >= 0) System.arraycopy(charArr, 0, map[i], 0, C);
        }

        for (int i = 0; i < R; i++) {
            map[i][0] = 'x';
            finished = false;
            dfs(i, 0);

        }

        System.out.println(ans);

    }

    static void dfs(int y, int x) {
        for (int i = 0; i < 3; i++) {
            if (!finished) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (0 <= ny && ny < R && 0 <= nx && nx < C && map[ny][nx] != 'x') {
                    map[ny][nx] = 'x';

                    if (nx == C - 1) {
                        ans += 1;
                        finished = true;
                        break;
                    }
                    dfs(ny, nx);
                }
            }
        }
    }
}
