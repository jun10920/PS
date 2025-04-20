import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        // 1) 그래프 입력
        List<Integer>[] adj = new ArrayList[N+1];
        int[] deg = new int[N+1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (true) {
                int x = Integer.parseInt(st.nextToken());
                if (x == 0) break;
                adj[i].add(x);
            }
            deg[i] = adj[i].size();
        }
        
        // 2) 초기화
        int[] time = new int[N+1];
        Arrays.fill(time, -1);
        int[] cnt = new int[N+1];  // i의 이웃 중 믿는 사람 수
        Queue<Integer> q = new ArrayDeque<>();
        
        // 최초 유포자
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int s = Integer.parseInt(st.nextToken());
            time[s] = 0;
            q.add(s);
        }
        
        // 3) BFS 전파 시뮬레이션
        while (!q.isEmpty()) {
            int u = q.poll();
            int t = time[u];
            for (int v : adj[u]) {
                if (time[v] != -1) continue;            // 이미 믿음
                if (++cnt[v] * 2 < deg[v]) continue;    // 아직 절반 미만
                time[v] = t + 1;                        // 이제 믿기 시작
                q.add(v);
            }
        }
        
        // 4) 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(time[i]).append(' ');
        }
        System.out.println(sb);
    }
}
