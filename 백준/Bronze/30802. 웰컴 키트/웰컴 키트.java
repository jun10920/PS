import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        int[] tArr = Arrays.stream(arr).mapToInt(Integer::parseInt).toArray();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int bunch = 0;
        for (int i : tArr) {
            if (i % T != 0) {
                bunch += i / T + 1;
            } else {
                bunch += i / T;
            }
        }
        
        System.out.println(bunch);
        System.out.print(n / P + " ");
        System.out.print(n % P);
    }
}