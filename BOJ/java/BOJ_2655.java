package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BOJ_2655 {
    int n;
    int[][] walls;
    int[][] counts;
    int[] dx = {0, 0, -1, 1};
    int[] dy = {-1, 1, 0 ,0};

    public BOJ_2655() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        this.n = Integer.parseInt(br.readLine());

        this.walls = new int[n][n];
        this.counts = new int[n][n];

        for (int y=0; y<n; y++) {
            char[] input = br.readLine().trim().toCharArray();
            for (int x=0; x < n; x++) {
                walls[y][x] = input[x] - '0';
                counts[y][x] = Integer.MAX_VALUE;
            }
            
        }
    }

    public void solve() {
        counts[0][0] = 0;
        Queue<int[]> q = new LinkedList<>(List.of(new int[]{0, 0, 0}));
        while (!q.isEmpty()) {
            int[] xyd = q.poll();
            int x = xyd[0];
            int y = xyd[1];
            int count = xyd[2];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < this.n && ny < this.n && this.counts[ny][nx] > this.counts[y][x]) {
                    if (walls[ny][nx] == 1) this.counts[ny][nx] = this.counts[y][x];
                    else this.counts[ny][nx] = this.counts[y][x] + 1;
                    q.add(new int[]{nx, ny, this.counts[ny][nx]});
                }
            }
        }
        System.out.println(counts[n-1][n-1]);
    }
}
