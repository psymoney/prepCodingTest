use std::io::*;

fn main() {
    let t = get_usize_from_line();

    for _ in 0..t {
        let min_max = get_min_and_max_from_input();
        println!("{} {}", min_max.0, min_max.1);
    }
}

fn get_min_and_max_from_input() -> (isize, isize) {
    let n = get_usize_from_line();
    let numbers = get_line().split_ascii_whitespace().map(|e| e.parse::<isize>().unwrap()).collect::<Vec<isize>>();

    get_min_and_max(numbers)
}

fn get_min_and_max(numbers: Vec<isize>) -> (isize, isize) {
    let mut min_max = (numbers[0], numbers[0]);

    for i in 1..numbers.len() {
        if numbers[i] < min_max.0 {min_max.0 = numbers[i]}
        if numbers[i] > min_max.1 {min_max.1 = numbers[i]}
    }

    min_max
}

fn get_usize_from_line() -> usize {
    to_usize(get_line())
}

fn get_line() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf.trim().to_string()
}

fn to_usize(v: String) -> usize {
    v.parse::<usize>().unwrap()
}
