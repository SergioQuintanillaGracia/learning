fn main() {
    let apples = 50;
    let oranges = 14 + 6;
    let fruits = apples + oranges;

    println!("This year, my garden has {0} apples", apples);
    println!("This year, my garden has {apples} apples");
    println!(
        "My garden has {0} apples and {1} fruits. Yes, I have {0} apples",
        apples, fruits
    );
}
