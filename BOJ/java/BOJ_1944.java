package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1944 {
    static int n, m;
    static char[][] board;
    static ArrayList<Node> nodes = new ArrayList<>();
    static PriorityQueue<Edge> pq;
    static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);
        board = new char[n][n];
        pq = new PriorityQueue<>();

        for(int y = 0; y < n; y++) {
            char[] line = br.readLine().trim().toCharArray();
            board[y] = line;
            for(int x = 0; x < n; x++) {
                if(line[x] == 'S' || line[x] == 'K') {
                    nodes.add(new Node(x, y));
                }
            }
        }
        for(int i = 0; i < m; i++) {
            bfs(i);
        }

        System.out.println(kruskal());
    }

    private static void bfs(int idx) {
        int[][] dist = new int[n][n];
        for(int i = 0; i < n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);
        int[] dx = new int[] {0, 0, -1, 1};
        int[] dy = new int[] {-1, 1, 0, 0};

        Queue<Node> q = new LinkedList<>();
        q.add(nodes.get(idx));
        dist[nodes.get(idx).y][nodes.get(idx).x] = 0;

        while(!q.isEmpty()) {
            Node current = q.poll();

            for(int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n || board[ny][nx] == '1') continue;
                int nd = dist[current.y][current.x] + 1;
                if(nd >= dist[ny][nx]) continue;
                dist[ny][nx] = nd;
                if(board[ny][nx] == 'K' || board[ny][nx] == 'S') {
                    for(int j = 0; j < nodes.size(); j++) {
                        if(nodes.get(j).x == nx && nodes.get(j).y == ny) {
                            pq.offer(new Edge(idx, j, dist[ny][nx]));
                        }
                    }
                }

                q.offer(new Node(nx, ny));
            }
        }
    }

    private static int kruskal() {
        parents = new int[m + 1];
        for(int i = 0; i < m + 1; i++) parents[i] = i;
        int totalCost = 0;
        int connections = 0;

        while(!pq.isEmpty()) {
            Edge current = pq.poll();

            int s = find(current.s);
            int e = find(current.e);

            if(s != e) {
                union(s, e);
                totalCost += current.cost;
                connections++;
            }
        }
        if(connections != m) return -1;
        return totalCost;
    }

    private static int find(int node) {
        if(parents[node] == node) return node;
        else return parents[node] = find(parents[node]);
    }

    private static void union(int s, int e) {
        parents[s] = e;
    }

    static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Edge implements Comparable<Edge> {
        int s, e;
        int cost;

        public Edge(int s, int e, int cost) {
            this.s = s;
            this.e = e;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return this.cost - o.cost;
        }
    }
}
