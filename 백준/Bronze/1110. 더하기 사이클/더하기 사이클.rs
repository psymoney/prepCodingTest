use std::io::*;

fn main() {
    let mut _in = String::new();

    stdin().read_line(&mut _in).unwrap();

    let init = _in.trim().parse::<usize>().unwrap();

    println!("{}", solve(init))
}

fn solve(init: usize) -> isize {
    let mut cnt = 0;
    let mut next = init.clone();

    loop {
        cnt += 1;
        next = next % 10 * 10 + (next / 10 + next % 10) % 10;

        if next == init {
            break;
        }
    }

    cnt
}