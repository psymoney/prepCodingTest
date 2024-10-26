package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_13905 {
    static class Edge implements Comparable<Edge> {
        int from, to, cost;

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
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parents = new int[n + 1];
        edges = new PriorityQueue<>();

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            Edge edge = new Edge(from, to, cost);
            edges.offer(edge);
        }

        // handle input ended
        initiateParents(n);
        System.out.println(kruskal(s, e));
    }

    static int kruskal(int s, int e) {
        int cost = 0;
        while (!edges.isEmpty()) {
            Edge current = edges.poll();
            cost = current.cost;
            union(find(current.from), find(current.to));
            if (find(s) == find(e)) break;
        }
        if(parents[s] != parents[e]) cost = 0;
        return cost;
    }

    static int find(int idx) {
        if(idx == parents[idx]) return idx;
        else return parents[idx] = find(parents[idx]);
    }

    static void union(int s, int e) {
        int sRoot = find(s);
        int eRoot = find(e);

        if(sRoot <= eRoot) {
            parents[eRoot] = sRoot;
        } else {
            parents[sRoot] = eRoot;
        }
    }

    static void initiateParents(int n) {
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
        }
    }
}
