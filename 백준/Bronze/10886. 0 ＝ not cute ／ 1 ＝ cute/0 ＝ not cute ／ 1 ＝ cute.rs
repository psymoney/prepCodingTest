use std::io::*;

fn main() -> Result<()> {
    let mut input = String::new();

    stdin().read_line(&mut input).unwrap();
    let n: u8 = input.trim().parse::<u8>().unwrap();

    let mut votes: [u8;2] = [0, 0];

    for _ in 0..n {
        let mut vote: String = String::new();
        
        stdin().read_line(&mut vote).unwrap();
        
        if vote.trim().parse::<u8>().unwrap() == 0 {
            votes[0] += 1;   
        } else {
            votes[1] += 1;
        }
    }

    if votes[0] > votes[1] {
        println!("Junhee is not cute!");
    } else {
        println!("Junhee is cute!");
    }

    Ok(())
}
