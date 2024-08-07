

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());

            int[] arr = new int[3];

            for (int i = 0; i < 3; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
                break;
            }

            Arrays.sort(arr);

            if (isRectangle(arr)) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }

    private static boolean isRectangle(int[] arr) {
        int a = arr[0];
        int b = arr[1];
        int c = arr[2];

        if ((a * a + b * b) == c * c) {
            return true;
        }
        return false;
    }
}