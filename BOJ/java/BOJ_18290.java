package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_18290 {
    static int[][] board;
    static int k, n, m, max = 0;
    static int[] dx = {-1, 1, -1, 1};
    static int[] dy = {-1, -1, 1, 1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[m][n];
        for (int i = 0; i < m; i++) {
            board[i] = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                max = Math.max(max, bfs(x, y, board[y][x], 1));
            }
        }

        System.out.println(max);
    }

    static int bfs(int x, int y, int sum, int cnt) {
        int max = 0;
        boolean[][] visited = new boolean[n][m];
        visited[y][x] = true;

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y, sum, cnt});

        while (!q.isEmpty()) {
            int[] curr = q.poll();

            // if the number is added k times then update max and skip this iteration
            if (curr[3] == k) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = curr[0] + dx[i];
                int ny = curr[1] + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    int next = board[ny][nx];
                    if (board[ny][nx] > 0) {
                        max = Math.max(max, curr[2] + next);
                        q.offer(new int[] {nx, ny, curr[2] + next, curr[3] + 1});
                    } else {
                        q.offer(new int[] {nx, ny, curr[2], curr[3]});
                    }
                }
            }
        }

        return max;
    }
}
