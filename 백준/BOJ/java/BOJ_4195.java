package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_4195 {
    static class Node {
        HashSet<String> friends;

        public Node(String friend) {
            friends = new HashSet<>();
            friends.add(friend);
        }

        public void addFriend(String friend) {
            friends.add(friend);
        }

        public int getNumFriends() {
            return friends.size();
        }
    }

    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            solve();
        }
    }

    public static void solve() throws IOException {
        int f = Integer.parseInt(br.readLine());

        HashMap<String, Node> networks = new HashMap<>();

            for (int j = 0; j < f; j++) {
                st = new StringTokenizer(br.readLine());
                int numFriends = 0;

                String f1 = st.nextToken();
                String f2 = st.nextToken();

                if (networks.containsKey(f1)) {
                    networks.get(f1).addFriend(f2);
                    numFriends += networks.get(f1).getNumFriends();
                } else {
                    networks.put(f1, new Node(f2));
                    numFriends += 1;
                }

                if (networks.containsKey(f2)) {
                    networks.get(f2).addFriend(f1);
                    numFriends += networks.get(f2).getNumFriends();
                } else {
                    networks.put(f2, new Node(f1));
                    numFriends += 1;
                }
                System.out.println(numFriends);
            }
    }
}
