package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11687 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());

        int l = 1;
        int r = m * 5;
        boolean check = false;

        while (l <= r) {
            int mid = (l + r) / 2;
            int cnt = getNumberOfFive(mid);
            if (cnt > m) {
                r = mid - 1;
            } else if (cnt == m) {
                r = mid - 1;
                check = true;
            } else {
                l = mid + 1;
            }
        }

        if (check) {
            System.out.println(l);
        } else {
            System.out.println(-1);
        }
    }

    private static int getNumberOfFive(int mid) {
        int cnt = 0;

        for (int i = 5; i <= mid; i *= 5) {
            cnt += (mid / i);
        }

        return cnt;
    }
}
