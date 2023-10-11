package BOJ.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_20444 {

    public static void main(String[] args) throws Exception {
        System.out.println("Hello World!");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        long k = Long.parseLong(st.nextToken());

        long l = 0;
        long r = n / 2;

        while (l <= r) {
            long row = (l + r) / 2;
            long col = n - row;

            long total = (row + 1) * (col + 1);

            if (total == k) {
                System.out.println("YES");
                return;
            } else if (total > k) {
                r = row - 1;
            } else {
                l = row + 1;
            }
        }
        System.out.println("NO");
    }
}
