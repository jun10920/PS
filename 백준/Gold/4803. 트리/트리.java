import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static List<Integer>[] adj;
    static boolean[] visited, isTree;

    static void dfs(int curr, int parent, int root) {
        visited[curr] = true;
        for (int nxt : adj[curr]) {
            if (!visited[nxt]) {
                dfs(nxt, curr, root);
            }
            else if (nxt != parent) {
                isTree[root] = false; // 이미 방문한 이웃인데, 바로 부모 노드가 아니면 사이클이 있다는 의미
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int caseNum = 1;
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            if (n == 0 && m == 0) break;

            adj = new ArrayList[n+1];
            visited = new boolean[n+1];
            isTree = new boolean[n+1];
            for (int i = 1; i <= n; i++) {
                adj[i] = new ArrayList<>();
                isTree[i] = true;
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adj[u].add(v);
                adj[v].add(u);
            }

            int treeCount = 0;
            for (int u = 1; u <= n; u++) {
                if (!visited[u]) {
                    dfs(u, 0, u);
                    if (isTree[u]) treeCount++;
                }
            }

            if (treeCount == 0) {
                System.out.printf("Case %d: No trees.\n", caseNum);
            } else if (treeCount == 1) {
                System.out.printf("Case %d: There is one tree.\n", caseNum);
            } else {
                System.out.printf("Case %d: A forest of %d trees.\n", caseNum, treeCount);
            }
            caseNum++;
        }
    }
}
