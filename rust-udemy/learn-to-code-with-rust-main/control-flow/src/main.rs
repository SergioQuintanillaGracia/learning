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

    let mut seconds = 10;

    loop {
        if seconds <= 0 {
            println!("Ending");
            break;
        }

        if seconds % 2 == 0 {
            println!("{seconds} seconds (even number), skipping 3 seconds...");
            seconds -= 3;
            continue;
        }

        println!("Seconds left: {seconds}");
        seconds -= 1;
    }

    seconds = 5;

    while seconds > 0 {
        println!("Seconds: {seconds}");
        seconds -= 1;
    }
    println!("Finish");

    println!("Factorial of 5: {}", factorial(5));
}

fn even_or_odd(number: i32) {
    let result = if number % 2 == 0 { "even" } else { "odd" };

    println!("The number is {result}");
}

fn factorial(n: i32) -> i32 {
    if n <= 1 {
        1
    } else {
        n * factorial(n - 1)
    }
}
