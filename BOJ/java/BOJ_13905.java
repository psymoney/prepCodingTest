package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_13905 {
    static class Node {
        private int maxWeight = 0;
        private ArrayList<int> adjacent;
        private ArrayList<int> costs;

        public Node(int adjacent, int cost) {
            this.adjacent = new ArrayList<int>(List.of(adjacent));
            this.costs = new ArrayList<int>(List.of(cost));
        }

        public void addAdjacent(int adjacent, int cost) {
            this.adjacent.add(adjacent);
            this.costs.add(cost);
        }

        public int updateMaxWeight(int weight) {
            if(weight > maxWeight) {
                maxWeight = weight;
            }
            return maxWeight;
        }

        public int getMaxWeight() {
            return maxWeight;
        }
    }

    static private HashMap<Integer, Node> nodes;

    public static void main(String[] args) throws IOException {
        // handle inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer firstInput = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(firstInput.nextToken());
        int m = Integer.parseInt(firstInput.nextToken());

        nodes = new HashMap<>();

        StringTokenizer secondInput = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(secondInput.nextToken());
        int e = Integer.parseInt(secondInput.nextToken());

        for(int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            if(nodes.containsKey(Integer.parseInt(input[0]))) {
                nodes.get(Integer.parseInt(input[0])).addAdjacent(Integer.parseInt(input[1]), Integer.parseInt(input[2]));
            } else {
                nodes.put(Integer.parseInt(input[0]), new Node(Integer.parseInt(input[1]), Integer.parseInt(input[2])));
            }
            if(nodes.containsKey(Integer.parseInt(input[1]))) {
                nodes.get(Integer.parseInt(input[1])).addAdjacent(Integer.parseInt(input[0]), Integer.parseInt(input[2]));
            } else {
                nodes.put(Integer.parseInt(input[1]), new Node(Integer.parseInt(input[0]), Integer.parseInt(input[2])));
            }
        }


    }

    private static void bfs(int s) {
        Queue<Integer> q = new LinkedList<>();
        q.add(s);

        while(!q.isEmpty()) {
            int n = q.poll();
            Node current = nodes.get(n);


        }
    }
}
