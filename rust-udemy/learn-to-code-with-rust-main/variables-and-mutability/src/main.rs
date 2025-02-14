const TAX_RATE: f32 = 72.25;


fn main() {
    let apples = 50;
    let oranges = 14 + 6;
    let mut fruits = apples + oranges;

    println!("This year, my garden has {0} apples", apples);
    println!("This year, my garden has {apples} apples");
    println!(
        "My garden has {0} apples and {1} fruits. Yes, I have {0} apples",
        apples, fruits
    );

    fruits = 100;
    println!("I now have {fruits} fruits");


    let grams = "100.345";
    let grams = 100.345;

    let mut grams = 100;
    grams = 101;
    let grams = 102;

    // grams = 103;  // (can't be done, as the variable is no longer mutable)

    println!("Grams outside after: {grams}");

    {
        // Not an example of variable shadowing, we are creating a different
        // grams variable inside the block
        let grams = 200;
        println!("Grams inside: {grams}");
    }

    println!("Grams outside after: {grams}");


    let income = 100000;
    println!("My income is {income} and my tax rate is {TAX_RATE}");
}
