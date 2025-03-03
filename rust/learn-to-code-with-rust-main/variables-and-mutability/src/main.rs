const TOUCHDOWN_POINTS: i32 = 6;

fn main() {
    let season: &str = "Winter";
    let mut points_scored: i32 = 28;

    points_scored = 35;

    let event_time = "06:00";
    let event_time = 6;

    println!("Season: {}  |  Points scored: {}", season, points_scored);
    println!("Season: {season}  |  Points scored: {points_scored}");
    println!("Season: {0}  |  Points scored: {1}", season, points_scored);

    #[allow(unused_variables)]
    let favorite_beverage = "water";
}