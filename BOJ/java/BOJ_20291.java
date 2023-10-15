package BOJ.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class BOJ_20291 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TreeMap<String, Integer> organizer = new TreeMap<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String ex = br.readLine().split("\\.")[1];

            if (!organizer.containsKey(ex)) {
                organizer.put(ex, 1);
            } else {
                organizer.replace(ex, organizer.get(ex) + 1);
            }
        }

        organizer.forEach((key, value) -> System.out.println(key + " " + value));
    }
}
