package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1032 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String answer = br.readLine();

        for (int i = 0; i < n - 1; i++) {
            String stringToComp = br.readLine();

            for (int j = 0; j < answer.length(); j++) {
                if (answer.charAt(j) != stringToComp.charAt(j)) {
                    answer = answer.substring(0, j) + '?' + answer.substring(j + 1);
                }
            }
        }

        System.out.println(answer);
    }
}
