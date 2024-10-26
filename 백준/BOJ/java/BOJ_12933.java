package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_12933 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(solve(br.readLine()));
    }

    static int solve(String sound) {
        // if the length of input is not multiple of 5, the input is not valid
        if (sound.length() % 5 != 0) {
            return -1;
        }

        int[] ducks = new int[5];

        for (char c: sound.toCharArray()) {
            int idx = "quack".indexOf(c);

            if (c == 'q') {
                if (ducks[4] > 0) ducks[4]--;
                ducks[0]++;
            } else {
                if (ducks[idx-1] == 0) return -1;
                ducks[idx-1]--;
                ducks[idx]++;
            }
        }

        // if all ducks is not finished by "quack" input is not valid
        if (ducks[0] > 0 || ducks[1] > 0 || ducks[2] > 0 || ducks[3] > 0) return -1;

        return ducks[4];
    }
}
