/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.io.*;
import java.util.*;

public class Solution {
    static int T;
    static char[] map;
    static StringBuilder sb = new StringBuilder();
    static Node[] nodes;
    static ArrayList<Integer> ans1;
    static ArrayList<Integer> ans2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        T = Integer.parseInt(br.readLine());
        int originalT = T;
        while (T-- > 0) {

            String[] inputs = br.readLine().split(" ");
            int V = Integer.parseInt(inputs[0]);
            int E = Integer.parseInt(inputs[1]);
            int node1  = Integer.parseInt(inputs[2]);
            int node2 = Integer.parseInt(inputs[3]);

            nodes = new Node[V + 1];
            for (int i = 0; i < V + 1; i++) {
                nodes[i] = new Node();
            }

            String[] temp = br.readLine().split(" ");
            int n = temp.length;
            int[] EList = new int[n];

            for (int i = 0; i < n; i++) {
                EList[i] = Integer.parseInt(temp[i]);
            }

            for (int i = 0; i < E * 2; i += 2) {
                int p = EList[i];
                int c = EList[i + 1];

                nodes[p].children.add(c);
                nodes[c].parent = p;
            }

            ans1 = new ArrayList<>();
            ans2 = new ArrayList<>();

            findAns(node1, ans1);
            findAns(node2, ans2);

            int ans = 0;
            for (int i = 0; i < V; i++) {
                if (!ans1.get(i).equals(ans2.get(i))) break;
                ans = ans1.get(i);
            }

            // 출력
            sb.append("#").append(originalT - T).append(" ").append(ans).append(" ").append(dfs(ans)).append("\n");
        }
        System.out.println(sb);
    }

    static int dfs(int idx) {
        int res = 1;
        for (int child : nodes[idx].children) {
            res += dfs(child);
        }
        return res;
    }

    static void findAns(int cur, ArrayList<Integer> ans) {
        int parent = nodes[cur].parent;
        if (parent != 0) {
            findAns(parent, ans);
        }
        ans.add(cur);
    }

    static class Node{
        List<Integer> children;
        int parent;

        Node() {
            this.children = new ArrayList<>();
            this.parent = 0;
        }
    }
}
