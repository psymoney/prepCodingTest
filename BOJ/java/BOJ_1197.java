package BOJ.java;

import org.jetbrains.annotations.NotNull;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1197 {
    static int v;
    static int e;
    static int[] parents;
    static PriorityQueue<Edge> pq;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        pq = new PriorityQueue<>();

        for(int i = 0; i < e; i++) {
            String[] input = br.readLine().split(" ");
            pq.offer(new Edge(
                    Integer.parseInt(input[0]),
                    Integer.parseInt(input[1]),
                    Integer.parseInt(input[2])));
        }

        System.out.println(kruskal());
    }

    private static int kruskal() {
        parents = new int[v + 1];
        for(int i = 0; i <= v; i++) parents[i] = i;

        int totalCost = 0;

        while(!pq.isEmpty()) {
            Edge current = pq.poll();

            int s = find(current.s);
            int e = find(current.e);
            if(s != e) {
                union(s, e);
                totalCost += current.cost;
            }
        }

        return totalCost;
    }

    private static int find(int node) {
        if(parents[node] == node) return node;
        else return parents[node] = find(parents[node]);
    }

    private static void union(int s, int e) {
        parents[s] = e;
    }

    static class Edge implements Comparable<Edge> {
        int s;
        int e;
        int cost;

        public Edge(int s, int e, int cost) {
            this.s = s;
            this.e = e;
            this.cost = cost;
        }

        @Override
        public int compareTo(@NotNull Edge e) {
            return this.cost - e.cost;
        }
    }
}
