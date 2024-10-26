class Solution {
    int[][] grid;
    public int[][] largestLocal(int[][] grid) {
        this.grid = grid;
        int[][] answer = new int[grid.length - 2][grid.length - 2];
        for (int y = 1; y < grid.length - 1; y++) {
            for (int x = 1; x < grid.length -1; x++) {
                answer[y-1][x-1] = getLocalMax(x, y);
            }
        }
        return answer;
    }
    
    private int getLocalMax(int x, int y) {
        int localMax = 0;
        for (int j = y - 1; j < y + 2; j++) {
            for (int i = x - 1; i < x + 2; i++) {
                localMax = Math.max(localMax, this.grid[j][i]);
            }
        }
        return localMax;
    }
}