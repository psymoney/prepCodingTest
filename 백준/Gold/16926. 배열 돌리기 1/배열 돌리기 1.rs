use std::{cmp::min, collections::VecDeque, io::{self, BufRead}};


fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).unwrap();

    let mut inputs = buf.trim().split_whitespace()
            .map(|e| e.parse::<usize>().unwrap());
    
    let n = inputs.next().unwrap();
    let m = inputs.next().unwrap();
    let r = inputs.next().unwrap();

    buf.clear();

    let mut arr = Vec::<Vec<usize>>::with_capacity(n);
    for line in stdin.lock().lines().take(n) {
        let row = line.unwrap().split_whitespace().map(|e| e.parse::<usize>().unwrap()).collect();
        arr.push(row);
    }

    let answer = rotate_vec(arr, r);

    for line in answer {
        let str = line.into_iter().map(|v| v.to_string()).collect::<Vec<String>>().join(" ");
        println!("{str}");
    } 
}

fn rotate_vec(vec: Vec<Vec<usize>>, r: usize) -> Vec<Vec<usize>> {
    let mut rotated = vec![vec![0; vec[0].len()]; vec.len()];

    let n = rotated.len();
    let m = rotated[0].len();

    let level = min(n, m) / 2;

    for i in 0..level {
        let size = (n - i * 2 - 1) * 2 + (m - i * 2 - 1) * 2;
        let mut q = VecDeque::<usize>::new();
        
        for top in i..m - 1 - i {
            q.push_back(vec[i][top]);
        }

        for right in i..n - 1 - i {
            q.push_back(vec[right][m - 1 - i]);
        }

        for bottom in (i + 1..=m - 1 - i).rev() {
            q.push_back(vec[n - 1 - i][bottom]);
        }

        for left in (i + 1..=n - 1 - i).rev() {
            q.push_back(vec[left][i]);
        }
        
        q.rotate_left(r % size);

        for top in i..m - 1 - i {
            rotated[i][top] = q.pop_front().unwrap(); 
        }

        for right in i..n - 1 - i {
            rotated[right][m - 1 - i] = q.pop_front().unwrap();
        } 

        for bottom in (i + 1..=m - 1 - i).rev() {
            rotated[n - 1 - i][bottom] = q.pop_front().unwrap();
        }

        for left in (i + 1..=n - 1 - i).rev() {
            rotated[left][i] = q.pop_front().unwrap();
        }
    }

    rotated
}