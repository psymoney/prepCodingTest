impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let mut sorted_s1_chars: Vec<char> = s1.chars().collect();
        let mut sorted_s2_chars: Vec<char> = s2.chars().collect();
        let s1_chars = s1.chars();
        let s2_chars = s2.chars();
        let mut diff_char_cnt: usize = 0;

        sorted_s1_chars.sort();
        sorted_s2_chars.sort();

        if sorted_s1_chars != sorted_s2_chars {
            return false;
        }

        for (c1, c2) in s1_chars.zip(s2_chars) {
            if c1 != c2 {
                diff_char_cnt += 1;
            }
        }

        if diff_char_cnt == 0 || diff_char_cnt == 2 {
            true
        } else {
            false
        }
    }
}