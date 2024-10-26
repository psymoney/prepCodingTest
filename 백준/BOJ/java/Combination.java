package BOJ.java;

import java.util.ArrayList;

class Combination<T> {
    ArrayList<T> item;
    int n;
    int r;
    int[] now;
    ArrayList<ArrayList<T>> result;

    public Combination(ArrayList<T> item) {
        this.item = item;
        this.n = item.size();
    }

    public ArrayList<ArrayList<T>> getCombination(int r) {
        this.r = r;
        now = new int[r];
        result = new ArrayList<>();
        setCombinationResult(0, 0, 0);
        return result;
    }

    public void setCombinationResult(int depth, int index, int target) {
        if (depth == r) {
            ArrayList<T> temp = new ArrayList<>();
            for (int i : now) {
                temp.add(item.get(i));
            }
            result.add(temp);
            return;
        }

        if (target == n) return;
        now[index] = target;
        setCombinationResult(depth + 1, index + 1, target + 1);
        setCombinationResult(depth, index, target + 1);
    }
}