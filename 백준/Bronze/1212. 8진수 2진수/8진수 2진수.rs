use std::io::*;

fn main() {
    let mut buf = String::new();
    stdin().read_line(&mut buf).expect("Failed to read line");

    let octal = buf.trim();

    println!("{}", convert_octal_into_binary(octal));
}

fn convert_octal_into_binary(octal: &str) -> String {
    const MAP: [&str; 8] = ["000", "001", "010", "011", "100", "101", "110", "111"];

    let mut binary_string = String::with_capacity(octal.len() * 3);

    for (i, digit) in octal.chars().enumerate() {
        let idx = digit.to_digit(8).unwrap() as usize;

        if i == 0 {
            binary_string.push_str(MAP[idx].trim_start_matches('0'));
        } else {
            binary_string.push_str(MAP[idx]);
        }
    }
    
    if binary_string.is_empty() {
        "0".to_string()
    } else {
        binary_string
    }
}