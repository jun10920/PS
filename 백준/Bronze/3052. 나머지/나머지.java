import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb =  new StringBuilder();
        StringTokenizer st;

        HashSet<Integer> li = new HashSet<>();

        for (int i = 0; i < 10; i++) {
            int temp = Integer.parseInt(br.readLine());
            li.add(temp % 42);
        }
        System.out.println(li.size());
    }
}
