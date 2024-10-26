package BOJ.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_5597 {
    int[] nums;
    public BOJ_5597() throws IOException {
        int N = 28;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        this.nums = new int[N];
        for (int i = 0; i < N; i++) nums[i] = Integer.parseInt(br.readLine().trim());
        Arrays.sort(nums);
        for (int i = 1; i < N; i++) if(nums[i] - nums[i-1] > 1) System.out.println(nums[i] - 1);
        
    }
}
