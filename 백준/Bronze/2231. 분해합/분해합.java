import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int totalNum = Integer.parseInt(br.readLine());
        int result = 0;

        for (int i = 1; i < totalNum; i++) {
            int sum = i;
            int n = i;

            while (n != 0) {
                sum += n % 10;
                n /= 10;
            }

            if (sum == totalNum) {
                result = i;
                break;
            }
        }

        System.out.println(result);
    }
}
