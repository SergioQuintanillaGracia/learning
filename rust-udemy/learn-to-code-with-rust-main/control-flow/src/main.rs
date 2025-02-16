fn main() {
    if true {
        println!("This will print");
    }

    even_or_odd(7);

    let evaluation = true;

    match evaluation {
        true => println!("The value is true"),
        false => println!("The value is false"),
        _ => println!("Impossible"),
    }

    let val = match evaluation {
        true => 20,
        false => 40,
    };
    println!("{val}");

    let number = 8;

    match number {
        2 | 4 | 6 | 8 => println!("{number} is either 2, 4, 6 or 8"),
        _ => println!("Unexpected!"),
    }

    match number {
        x if x % 2 == 0 => println!("{x} is an even number"),
        x if x % 2 != 0 => println!("{x} is an odd number"),
        _ => unreachable!(),
    }
}

fn even_or_odd(number: i32) {
    let result = if number % 2 == 0 { "even" } else { "odd" };

    println!("The number is {result}");
}
