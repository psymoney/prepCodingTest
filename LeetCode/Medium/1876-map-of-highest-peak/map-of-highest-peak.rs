use std::collections::VecDeque;

impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = is_water.len();
        let cols = is_water[0].len();
        let mut deq: VecDeque<(usize, usize)> = VecDeque::new();
        let mut distance: Vec<Vec<i32>> = vec![vec![-1; cols]; rows];
        let directions: [(i32, i32); 4] = [(0, 1), (0, -1), (-1, 0), (1, 0)];

        for (y, row) in is_water.iter().enumerate() {
            for (x, col) in row.iter().enumerate() {
                if is_water[y][x] == 1 {
                    deq.push_back((x, y));
                    distance[y][x] = 0;
                }
            }
        }

        while let Some((x, y)) = deq.pop_front() {
            for (dx, dy) in directions {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;

                if nx >= 0 && ny >= 0 && nx < cols as i32 && ny < rows as i32 {
                    let nx = nx as usize;
                    let ny = ny as usize;

                    if distance[ny][nx] == -1 {
                        distance[ny][nx] = distance[y][x] + 1;
                        deq.push_back((nx, ny));
                    }
                }
            }
        }

        distance
    }
}