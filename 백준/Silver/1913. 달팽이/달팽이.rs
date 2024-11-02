use std::io::stdin;

fn main() {
    let mut input1 = String::new();
    let mut input2 = String::new();
    stdin().read_line(&mut input1).unwrap();
    stdin().read_line(&mut input2).unwrap();
    let n = input1.trim().parse::<usize>().unwrap();
    let v = input2.trim().parse::<usize>().unwrap();

    let (board, (y, x)) = generate_board(n, v);

    for line in board.iter() {
        let ss = line.into_iter().map(|c| c.to_string()).collect::<Vec<String>>().join(" ");
        println!("{ss}");
    }
    println!("{y} {x}");

}

fn generate_board(n: usize, v: usize) -> (Vec<Vec<usize>>, (usize, usize)) {
    let mut board = vec![vec![0 ;n]; n];
    let mut coordinates = (0 as usize, 0 as usize);
    
    let (mut x, mut y) = (n / 2 , n / 2);
    let mut value = 1;

    board[y][x] = value;

    if value == v {
        coordinates = (y + 1, x + 1);
    }

    value += 1;

    let directions: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

    for i in (2..n).step_by(2) {
        y -= 1;
        x -= 1;

        for &(dy, dx) in &directions {
            for _ in 0..i {
                y = (y as isize + dy) as usize;
                x = (x as isize + dx) as usize;


                board[y][x] = value;

                if value == v {
                    coordinates = (y + 1, x + 1);
                }

                value += 1;
            }
        }
    }

    (board, coordinates)
}


#[test]
fn with_three() {
    let expected = vec![vec![9, 2, 3], vec![8, 1 ,4], vec![7, 6, 5]];
    assert_eq!(generate_board(3, 2), (expected, (1 as usize, 2 as usize)));
}

#[test]
fn with_five() {
    let expected: Vec<Vec<usize>> = vec![
        vec![25, 10, 11, 12, 13],
        vec![24, 9, 2, 3, 14],
        vec![23, 8, 1, 4, 15],
        vec![22, 7, 6, 5, 16],
        vec![21, 20, 19, 18, 17]
    ];
    assert_eq!(generate_board(5, 17), (expected, (5 as usize, 5 as usize)));
}

#[test]
fn with_seven() {
    let expected: Vec<Vec<usize>> = vec![
        vec![49, 26, 27, 28, 29, 30, 31],
        vec![48, 25, 10, 11, 12, 13, 32],
        vec![47, 24, 9, 2, 3, 14, 33],
        vec![46, 23, 8, 1, 4, 15, 34],
        vec![45, 22, 7, 6, 5, 16, 35],
        vec![44, 21, 20, 19, 18, 17, 36],
        vec![43, 42, 41, 40, 39, 38, 37]
    ];
    assert_eq!(generate_board(7, 35), (expected, (5 as usize, 7 as usize)));
}
