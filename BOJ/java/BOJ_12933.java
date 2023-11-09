package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_12933 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sound = br.readLine();
        String quack = "quack";
        ArrayList<String> ducks = new ArrayList<>();

        // if the length of input is not multiple of 5, it's not valid
        if (sound.length() % 5 != 0) {
            System.out.println(-1);
            return;
        }
        
        for (char c: sound.toCharArray()) {
            int idx = quack.indexOf(c);
            boolean isNotExist = true;
            
            for (int i=0; i < ducks.size(); i++) {
                if (ducks.get(i).length() % 5 == idx) {
                    ducks.set(i, ducks.get(i) + c);
                    isNotExist = false;
                    break;
                }
            }
            
            if (idx == 0 && isNotExist) {
                ducks.add("q");
            } else if (idx != 0 && isNotExist) {
                System.out.println(-1);
                return;
            }
        }

        // if all ducks is not finished by "quack" input is not valid
        boolean r = true;
        for (String duck: ducks) {
            if (duck.length() % 5 != 0) {
                r = false;
                break;
            }
        }

        if (r) {
            System.out.println(ducks.size());
        } else {
            System.out.println(-1);
        }
    }
}
