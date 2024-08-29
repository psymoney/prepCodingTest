use std::io;

fn main() {
    let mut input = String::new();
    
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    
    let words: Vec<&str> = input.split_whitespace().collect();
    println!("{}", words.len());
}