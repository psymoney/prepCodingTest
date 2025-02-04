use std::cmp::max;

impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut answer: i32 = 0;

        let mut local_sum: i32 = 0;
        let mut prev: i32 = 0;

        for v in nums.iter() {
            if *v > prev {
                local_sum += *v;
            } else {
                answer = max(answer, local_sum);
                local_sum = *v;
            }
            prev = *v;
        }
        answer = max(answer, local_sum);

        answer
    }
}