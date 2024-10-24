use std::collections::{HashMap, VecDeque};
use std::io::*;
use std::result::Result;

fn main() {
    let (v_cnt, e_cnt) = _parse_two_integer(&_read_line()).unwrap();

    let edges = _collect_edges(e_cnt);

    let graph = _generate_graph(edges);

    let result = solve(v_cnt, graph);

    print!("{}", result)
}

fn solve(v: usize, graph: HashMap<usize, Vec<usize>>) -> usize {
    let mut visited = vec![false; v + 1];
    let mut cnt = v;

    for i in graph.keys() {
        if visited[*i] == true {
            cnt -= 1;
            continue;
        }
        visited[*i] = true;

        _check_visited_vertex_in_graph(*i, &graph, &mut visited);
    }

    cnt
}

fn _check_visited_vertex_in_graph(n: usize, graph: &HashMap<usize, Vec<usize>>, visited: &mut Vec<bool>) {
    let mut deque: VecDeque<usize> = VecDeque::from([n]);

    while deque.len() > 0 {
        let vertex: usize = deque.pop_front().unwrap();

        for adj in graph.get(&vertex).unwrap() {
            if visited[*adj] == false {
                deque.push_back(*adj);
                visited[*adj] = true;
            }
        }
    }
}

fn _read_line() -> String {
    let mut _in  = String::new();

    stdin().read_line(&mut _in).unwrap();

    _in
}

fn _collect_edges(e: usize) -> Vec<(usize, usize)> {
    let mut edges: Vec<(usize, usize)> = Vec::new();

    for _ in 0..e {
        let (v1, v2) = _parse_two_integer(&_read_line()).unwrap();
        edges.push((v1, v2));
    }

    edges
}

fn _parse_two_integer(line: &str) -> Result<(usize, usize), String> {
    if let Some((v_str, e_str)) = line.trim().split_once(' ') {
        let v = v_str.parse::<usize>().expect("Failed to parse integer");
        let e = e_str.parse::<usize>().expect("Failed to parse integer");

        Ok((v, e))
    } else {
        Err(format!("Invalid input '{}'", line))
    }
}

fn _generate_graph(edges: Vec<(usize, usize)>) -> HashMap<usize, Vec<usize>> {
    let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();

    for (e1, e2) in edges {
        graph.entry(e1).or_insert_with(Vec::new).push(e2);
        graph.entry(e2).or_insert_with(Vec::new).push(e1);
    }

    graph
}