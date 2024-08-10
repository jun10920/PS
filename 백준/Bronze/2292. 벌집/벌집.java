import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int layer = 1;  // 껍질 번호 (중앙 1번 방이 1층)
        int range = 2;  // 각 껍질의 최대 번호 (2번째 껍질의 시작은 2번 방)

        if (N == 1) {
            System.out.println(1);
        } else {
            while (range <= N) {
                range += 6 * layer;  // 각 껍질마다 방의 개수는 6의 배수로 늘어남
                layer++;
            }
            System.out.println(layer);
        }
    }
}
