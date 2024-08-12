

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int len = Integer.parseInt(br.readLine());
        String temp = br.readLine();

        int r = 31;
        int M = 1234567891;
        long result = 0;
        long power = 1;

        for (int i = 0; i < len; i ++) {
            int charValue = temp.charAt(i) - 'a' + 1;
            result = (result + charValue * power) % M;
            power = power * r % M;
        }
        System.out.println(result);
    }
}

