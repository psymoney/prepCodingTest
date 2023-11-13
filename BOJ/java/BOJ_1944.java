package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_1944 {
    int n;
    int m;
    char[][] board;
    int[][] dist;
    int[] s = new int[2];
    ArrayList<int[]> k = new ArrayList<>();

    public BOJ_1944() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);
        board = new char[n][n];
        dist = new int[n][n];

        for(int y = 0; y < n; y++) {
            char[] line = br.readLine().trim().toCharArray();
            board[y] = line;
            for(int x = 0; x < n; x++) {
                dist[y][x] = Integer.MAX_VALUE;

                if(line[x] == 'S') {
                    s = new int[] {x, y};
                } else if(line[x] == 'K') {
                    k.add(new int[] {x, y});
                }
            }
        }
        solve();
    }

    private void solve() {
        int[] dx = new int[] {0, 0, -1, 1};
        int[] dy = new int[] {-1, 1, 0, 0};

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {s[0], s[1], s[0], s[1]});
        dist[s[1]][s[0]] = 0;

        while (!q.isEmpty()) {
            int[] axis = q.poll();
            int x = axis[0];
            int y = axis[1];
            int sx = axis[2];
            int sy = axis[3];

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n || board[ny][nx] == '1') continue;
                if(ny == sy && nx == sx) continue;

                if(board[y][x] == 'K' && 1 < dist[ny][nx]) {
                    dist[ny][nx] = 1;
                    q.add(new int[] {nx, ny, sx, sy});
                } else if(board[y][x] != 'K' && dist[y][x] + 1 < dist[ny][nx]) {
                    dist[ny][nx] = dist[y][x] + 1;
                    if(board[ny][nx] == 'K') {
                        q.add(new int[] {nx, ny, nx, ny});
                    } else {
                        q.add(new int[] {nx, ny, sx, sy});
                    }
                }

            }
        }

        System.out.println(calculateTotalDist());
    }

    private int calculateTotalDist() {
        int total = 0;

        for(int i = 0; i < m; i++) {
            int x = k.get(i)[0];
            int y = k.get(i)[1];
            if(dist[y][x] == Integer.MAX_VALUE) {
                return -1;
            }
            total += dist[y][x];
        }

        return total;
    }
}
