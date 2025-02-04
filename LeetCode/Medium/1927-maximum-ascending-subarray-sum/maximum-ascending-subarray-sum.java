class Solution {
    public int maxAscendingSum(int[] nums) {
        int answer = 0;
        int localSum = 0;
        int prev = 0;

        for (int value: nums) {
            if (value > prev) {
                localSum += value;
            } else {
                answer = Math.max(answer, localSum);
                localSum = value;
            }

            prev = value;
        }

        answer = Math.max(answer, localSum);

        return answer;
    }
}