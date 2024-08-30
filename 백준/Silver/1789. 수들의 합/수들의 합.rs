use std::io::*;

fn main() -> Result<()> {
    let mut input = String::new();
    
    stdin().read_line(&mut input).unwrap();
    
    let s = input.trim().parse::<usize>().unwrap();
    
    let mut cnt = 0;
    let mut total = 0;
    
    for i in 1..s + 1 {
        total += i;
        cnt += 1;
        
        if total == s {
            break;
        } else if total > s {
            cnt -= 1;
            break;
        }
    }
    
    println!("{}", cnt);
    
    Ok(())
}