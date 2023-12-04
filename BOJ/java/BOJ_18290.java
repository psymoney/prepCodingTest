package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_18290 {
    static int[][] board;
    static boolean[][] picked;
    static int k, n, m, max = 0;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        picked = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        System.out.println(solve(0, 0, 0, 0));
    }

    static int solve(int x, int y, int cnt, int sum) {
        if (cnt == k) {
            return sum;
        }
        int max = Integer.MIN_VALUE;

        for (int r = y; r < n; r++) {
            for (int c = (r == y ? x : 0); c < m; c++) {
                if (!picked[r][c] && isNoAdjacentPicked(c, r)) {
                    picked[r][c] = true;
                    int result = solve(c, r, cnt + 1, sum + board[r][c]);
                    picked[r][c] = false;

                    max = Math.max(max, result);
                }
            }
        }

        return max;
    }

    static boolean isNoAdjacentPicked(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                if (picked[ny][nx]) return false;
            }
        }

        return true;
    }
}
