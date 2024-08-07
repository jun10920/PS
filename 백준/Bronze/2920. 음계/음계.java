

import java.io.*;
import java.util.*;

public class Main {

    public static boolean isUp(int[] arr) {
        for (int i = 0; i < 7; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public static boolean isDown(int[] arr) {
        for (int i = 0; i < 7; i++) {
            if (arr[i] < arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[8];

        for (int i = 0; i < 8; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (isUp(arr)) {
            System.out.println("ascending");
        } else if (isDown(arr)) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}

