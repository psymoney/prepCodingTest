package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class BOJ_9375 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            solve(Integer.parseInt(br.readLine()));
        }
    }

    static void solve(int n) throws IOException {
        HashMap<String, Integer> dresser = new HashMap<>();
        int answer = 1;

        for (int i = 0; i < n; i++) {
            String[] dress = br.readLine().split("\\s");
            if (dresser.containsKey(dress[1])) {
                dresser.replace(dress[1], dresser.get(dress[1]) + 1);
            } else {
                dresser.put(dress[1], 1);
            }
        }

        for (int val: dresser.values()) {
            answer *= (val + 1);
        }
        System.out.println(answer - 1);
    }
}