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
            if (c == 'q') {
                // if ducks array is empty then add a new element
                if (ducks.isEmpty()) {
                    ducks.add("q");
                } else {
                    // put a new element into ducks array or update the finished element
                    boolean isEmpty = true;

                    for (int i = 0; i < ducks.size(); i++) {
                        if (ducks.get(i).length() == 5) {
                            ducks.set(i, "q");
                            isEmpty = false;
                            break;
                        }
                    }

                    if (isEmpty) {
                        ducks.add("q");
                    }
                }
            } else {
                // check in which index the given character located
                int idx = quack.indexOf(c);
                // checker whether the matching duck exists
                boolean isNotExist = true;

                // iterate array ducks, and update the matching duck
                for (int i=0; i < ducks.size(); i++) {
                    if (ducks.get(i).length() == idx) {
                        ducks.set(i, ducks.get(i) + c);
                        isNotExist = false;
                        break;
                    }
                }

                // if there is no matching duck, input data is not valid
                if (isNotExist) {
                    System.out.println(-1);
                    return;
                }
            }
        }

        // if all ducks is not finished by "quack" input is not valid
        boolean r = true;
        for (String duck: ducks) {
            if (duck.length() != 5) {
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
