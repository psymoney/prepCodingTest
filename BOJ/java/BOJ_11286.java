package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BOJ_11286 {

    static PriorityQueue<Integer> plusPq;
    static PriorityQueue<Integer> minusPq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        plusPq = new PriorityQueue<>();
        minusPq = new PriorityQueue<>(Comparator.reverseOrder());

        for(int i = 0; i < n; i++) {
            int v = Integer.parseInt(br.readLine());
            if(v < 0) minusPq.offer(v);
            else if(v > 0) plusPq.offer(v);
            else System.out.println(pop());
        }
    }

    private static int pop() {
        if(plusPq.isEmpty() && minusPq.isEmpty()) return 0;
        if(plusPq.isEmpty()) return minusPq.poll();
        if(minusPq.isEmpty()) return plusPq.poll();

        int pV = Math.abs(plusPq.peek());
        int mV = Math.abs(minusPq.peek());

        if(pV < mV) return plusPq.poll();
        else if(mV < pV) return minusPq.poll();
        else return minusPq.poll();
    }
}
