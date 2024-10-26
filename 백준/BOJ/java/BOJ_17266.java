package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ_17266 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        ArrayList<String> strPos = new ArrayList<>(Arrays.asList(br.readLine().split("\\s")));
        ArrayList<Integer> pos = new ArrayList<>();
        for(String e: strPos) pos.add(Integer.parseInt(e));
        int optH = 0;

        optH = Math.max(pos.get(0), n - pos.get(pos.size() - 1));

        for (int i = 1; i < pos.size(); i ++) {
            int len = Math.round(((float)(pos.get(i) - pos.get(i-1)) / 2));
            optH = Math.max(optH, len);
        }

        System.out.println(optH);
    }
}
