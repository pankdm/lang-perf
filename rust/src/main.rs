use std::env;
use std::fs;
use std::str;
use std::collections::VecDeque;
use std::time::{Duration, Instant};

type Graph = Vec<Vec<i32>>;

#[derive(Debug)]
struct Input {
    graph: Graph,
    mines: Vec<String>,
    num_cities: i32,
}

impl Input {
    pub fn new() -> Self {
        Input {
            graph: vec![],
            mines: vec![],
            num_cities: 0,
        }
    }
}

fn read_i32(lines: &mut str::Lines) -> i32 {
    lines.next().unwrap().parse::<i32>().unwrap()
}

fn read_from_file(filename: &String) -> Input {
    let text = fs::read_to_string(filename).expect(&format!("Error reading file {}", filename));
    let mut input = Input::new();
    // println!("{}", text);
    let mut lines = text.lines();
    let num_cities: i32 = read_i32(&mut lines);

    input.num_cities = num_cities;
    input.graph.resize(num_cities as usize, vec![]);

    let num_mines: i32 = read_i32(&mut lines);
    // skip mines line
    lines.next();
    // for i in 0..num_mines {
    //     // do nothing
    //     lines.next();
    // }

    let num_edges: i32 = read_i32(&mut lines);
    for _ in 0..num_edges {
        let edge: Vec<&str> = lines.next().unwrap().split(" ").collect();
        // println!("{:?}", edge);
        let s: i32 = edge[0].parse().unwrap();
        let t: i32 = edge[1].parse().unwrap();
        input.graph[s as usize].push(t);
        input.graph[t as usize].push(s);
    }

    input
}

const NOT_PROCESSED: i32 = -1;

fn run_bfs(start: i32, input: &Input, scores: &mut Vec<i32>) {
    scores.resize(input.num_cities as usize, NOT_PROCESSED);
    scores[start as usize] = 0;

    let mut queue: VecDeque<i32> = VecDeque::new();
    queue.push_back(start);

    while !queue.is_empty() {
        let now = queue.pop_front().unwrap();
        let value = scores[now as usize];

        for next in input.graph[now as usize].iter() {
            if scores[*next as usize] == NOT_PROCESSED {
                scores[*next as usize] = value + 1;
                queue.push_back(*next);
            }
        }
    }
}


fn compute_hash(input: &Input) {
   let now = Instant::now();

    let mut distances: Vec<Vec<i32>> = vec![];
    distances.resize(input.num_cities as usize, vec![]);

    for i in 0..input.num_cities {
        run_bfs(i, &input, &mut distances[i as usize]);
    }

    let mut total_score: i32 = 0;
    for i in 0..input.num_cities {
        let mut current_score: i32 = 0;
        for d in distances[i as usize].iter() {
            if *d == NOT_PROCESSED {
                continue;
            }
            let d2 = d * d;
            current_score ^= d2;
        }
        total_score += current_score;
    }
    println!("graph_hash={}", total_score);

    let elapsed = now.elapsed().as_micros();
    println!("time={}", elapsed as f64 / 1000 as f64);

}

fn main() {
    // println!("Hello, world!");
    let args: Vec<String> = env::args().collect();
    assert!(
        args.len() >= 2,
        format!("Expecting at least 2 arguments for {:?}", args)
    );

    let input = read_from_file(&args[1]);
    // println!("{:?}", input);
    compute_hash(&input);
}
