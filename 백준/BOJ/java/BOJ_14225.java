//package BOJ.java;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.Arrays;
//
//public class BOJ_14225 {
//    static class Combination {
//        int[][] combination;
//
//        public Combination(int[] arr, int r) {
//
//        }
//    }
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int n = Integer.parseInt(br.readLine());
//        char[] input = br.readLine().trim().replaceAll(" ", "").toCharArray();
//        int[] seq = new int[input.length];
//        int sumTotal = 0;
//        for (int i = 0; i < input.length; i++) {
//            seq[i] = input[i] - '0';
//            sumTotal += seq[i];
//        }
//        Arrays.sort(seq);
//
//        for (int r = 1; r <= seq.length; r++) {
//            int[][] combi = combination(seq.clone(), new boolean[seq.length], 0, r);
//        }
//
//    }
//
//    private static int[][] combination(int[] arr, boolean[] visited, int start, int r) {
//        if (r == 0) {
//            int[][] combi = new int[arr.length][r];
//
//            for (int i = 0; i < arr.length; i++) {
//                if (visited[i])
//            }
//
//            return combi;
//        }
//    }
//}
