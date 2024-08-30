use std::io::*;

fn main() -> Result<()> {
    let mut input = String::new();
    
    stdin().read_line(&mut input).unwrap();
    
    let dishes: Vec<char> = input.trim().chars().collect();
 
    let mut height = 10;
    
    for i in 1..dishes.len() {
        if dishes[i] == dishes[i - 1] {
            height += 5;
        } else {
            height += 10;
        }
    }
    
    println!("{}", height);
    
    Ok(())
}