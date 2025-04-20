import java.io.*;
import java.util.*;

public class Main {
    static class Room { int x, y, price;
        Room(int x,int y,int p){this.x=x;this.y=y;this.price=p;} }
    static class Point { int x, y;
        Point(int x,int y){this.x=x;this.y=y;}
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        List<Room> rooms = new ArrayList<>();
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            rooms.add(new Room(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }

        int[][] dist = new int[N+1][M+1];
        for (int i = 1; i <= N; i++) Arrays.fill(dist[i], -1);

        Queue<Point> q = new ArrayDeque<>();
        for (int i = 0; i < C; i++) {
            st = new StringTokenizer(br.readLine());
            int cx = Integer.parseInt(st.nextToken());
            int cy = Integer.parseInt(st.nextToken());
            dist[cx][cy] = 0;
            q.add(new Point(cx, cy));
        }

        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int k = 0; k < 4; k++) {
                int nx = p.x + dx[k], ny = p.y + dy[k];
                if (nx<1 || nx> N || ny<1 || ny> M) continue;
                if (dist[nx][ny] != -1) continue;
                dist[nx][ny] = dist[p.x][p.y] + 1;
                q.add(new Point(nx, ny));
            }
        }

        long answer = Long.MAX_VALUE;
        for (Room rm : rooms) {
            long d = dist[rm.x][rm.y];
            answer = Math.min(answer, d * rm.price);
        }
        System.out.println(answer);
    }
}
