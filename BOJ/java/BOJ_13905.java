package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_13905 {
    static class Edge implements Comparable<Edge> {
        int from;
        int to;
        int cost;

        public Edge(int from, int to, int cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return (this.cost - o.cost) * -1;
        }
    }
    static int[] parents;
    static PriorityQueue<Edge> edges;

    public static void main(String[] args) throws IOException {
        // handle inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer firstInput = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(firstInput.nextToken());
        int m = Integer.parseInt(firstInput.nextToken());

        parents = new int[n + 1];
        for(int i = 0; i <= n; i++) parents[i] = i;
        edges = new PriorityQueue<>();

        StringTokenizer secondInput = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(secondInput.nextToken());
        int e = Integer.parseInt(secondInput.nextToken());

        for(int i = 0; i < m; i++) {
            char[] input = br.readLine().trim().replaceAll(" ", "").toCharArray();
            edges.offer(new Edge(input[0] - '0', input[1] - '0', input[2] - '0'));
        }
        // handle input ended

        System.out.println(kruskal(s, e));
    }

    static int kruskal(int s, int e) {
        int cost = 0;
        while(!edges.isEmpty()) {
            Edge current = edges.poll();

            cost = current.cost;
            int from = find(current.from);
            int to = find(current.to);

            if(from != to) {
                union(from, to);
            } else continue;

            if(find(s) == find(e)) break;
        }

        if(parents[s] != parents[e]) cost = 0;

        return cost;
    }

    static int find(int idx) {
        if(idx == parents[idx]) return idx;
        else return parents[idx] = find(parents[idx]);
    }

    static void union(int s, int e) {
        if(s < e) {
            parents[e] = s;
        } else {
            parents[s] = e;
        }
    }
}
