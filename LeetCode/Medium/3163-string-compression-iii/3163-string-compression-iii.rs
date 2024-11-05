impl Solution {
    pub fn compressed_string(word: String) -> String {
        let mut comp = String::new();

        let mut prev = word.chars().nth(0).unwrap();
        let mut cnt = 0;

        for (i, ch) in word.char_indices() {
            if ch == prev && cnt < 9 {
                cnt += 1;
            } else {
                comp.push(char::from_digit(cnt as u32, 10).unwrap());
                comp.push(prev);
                cnt = 1;
            }
            prev = ch;
        }
        comp.push(char::from_digit(cnt as u32, 10).unwrap());
        comp.push(prev);

        comp
    }
}