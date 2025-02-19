import java.util.*;
import java.io.*;

public class Main {

	static int N; // 물품의 수
	static int K; // 준서가 버틸 수 있는 무게
	static int[][] items;
	static int[][] dp;
	
	static int dfs(int idx, int curW) {
		
		if(curW >= K) {
			return 0;
		}
		
		if(idx == N) {
			return 0;
		}
		
		if(dp[idx][curW] != -1) {
			return dp[idx][curW];
		}
		
		int weight = items[idx][0];
		int value = items[idx][1];
		int ret = Integer.MIN_VALUE;
		
		if (curW + weight <= K) {
			ret = Math.max(ret,  dfs(idx + 1, curW + weight) + value);
		}
		
		ret = Math.max(ret, dfs(idx + 1, curW));
		
		dp[idx][curW] = ret;
		return ret;
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		items = new int[N][2];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			items[i][0] = Integer.parseInt(st.nextToken());
			items[i][1] = Integer.parseInt(st.nextToken());
		}
		
		dp = new int[N][K + 1];
		for (int i = 0; i < N; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		int answer = dfs(0, 0);
		
		System.out.println(answer);
	}

}
