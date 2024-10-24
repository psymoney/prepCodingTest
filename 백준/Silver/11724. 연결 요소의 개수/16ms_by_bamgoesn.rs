#![no_main]

#[no_mangle]
fn main() -> i32 {
    // FastIO
    use fastio::*;
    let input_str = get_input();
    let mut sc: Splitter<_> = Splitter::new(input_str, |s| s.split_ascii_whitespace());

    // FastIO Macros
    macro_rules! next {
        () => { sc.next() };
        ($($t:ty) +) => { ($(sc.next::<$t>()),+) };
    }

    // Main
    let (n, m) = next!(usize usize);
    let mut uf = UnionFind::new(n);
    for _ in 0..m {
        let (u, v) = next!(usize usize);
        uf.union(u - 1, v - 1);
    }

    println!("{}", uf.get_group_num());
    0
}

struct UnionFind {
    size: usize,
    parents: Vec<usize>,
    group_size: Vec<usize>,
    group_num: usize,
}

impl UnionFind {
    /// Returns a new UnionFind instance where `size` number of elements are in their own disjoint set.
    fn new(size: usize) -> Self {
        Self {
            size,
            parents: vec![size; size],
            group_size: vec![1; size],
            group_num: size,
        }
    }

    /// Returns the number of nodes which can be reached from x.
    fn get_group_size(&mut self, x: usize) -> usize {
        let root = self.find_root(x);
        self.group_size[root]
    }

    /// Returns the number of connected components.
    fn get_group_num(&self) -> usize {
        self.group_num
    }

    fn find_root(&mut self, x: usize) -> usize {
        if self.parents[x] == self.size {
            return x;
        }
        let root = self.find_root(self.parents[x]);
        self.parents[x] = root;
        root
    }

    /// Returns true if there exists a path from a to b.
    fn is_reachable(&mut self, a: usize, b: usize) -> bool {
        self.find_root(a) == self.find_root(b)
    }

    /// Add an edge between a and b.
    fn union(&mut self, a: usize, b: usize) {
        let a_root = self.find_root(a);
        let b_root = self.find_root(b);

        if a_root != b_root {
            self.group_num -= 1;
            let a_size = self.group_size[a_root];
            let b_size = self.group_size[b_root];
            if a_size < b_size {
                self.parents[a_root] = b_root;
                self.group_size[b_root] += a_size;
            } else {
                self.parents[b_root] = a_root;
                self.group_size[a_root] += b_size;
            }
        }
    }
}

mod fastio {
    use std::{slice::*, str::*};

    #[link(name = "c")]
    extern "C" {
        fn mmap(addr: usize, len: usize, p: i32, f: i32, fd: i32, o: i64) -> *mut u8;
        fn fstat(fd: i32, stat: *mut usize) -> i32;
    }

    pub fn get_input() -> &'static str {
        let mut stat = [0; 20];
        unsafe { fstat(0, stat.as_mut_ptr()) };
        let buffer = unsafe { mmap(0, stat[6], 1, 2, 0, 0) };
        unsafe { from_utf8_unchecked(from_raw_parts(buffer, stat[6])) }
    }

    pub struct Splitter<I: Iterator> {
        it: I,
    }

    impl<'a, 'b: 'a, T: Iterator> Splitter<T> {
        pub fn new(s: &'b str, split: impl FnOnce(&'a str) -> T) -> Self {
            Self { it: split(s) }
        }
    }

    impl<'a, I: Iterator<Item = &'a str>> Splitter<I> {
        pub fn next<T: FromStr>(&mut self) -> T {
            self.it.next().unwrap().parse().ok().unwrap()
        }
    }
}
