package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class BOJ_14425 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);

        HashMap<String, Integer> hm = new HashMap<>();
        int answer = 0;

        for (int i = 0; i < n; i++) {
            hm.put(br.readLine(), 0);
        }

        for (int i = 0; i < m; i++) {
            String key = br.readLine();
            if (hm.containsKey(key)) {
                hm.put(key, hm.get(key) + 1);
            }
        }

        for (String key: hm.keySet()) {
            answer += hm.get(key);
        }

        System.out.println(answer);
    }
}
