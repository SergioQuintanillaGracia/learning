fn main() {
    print_string("hello");

    let val = 5;
    println!("Square of {val} = {}", square(val));
    println!("Square of {val} = {}", square_implicit(val));

    let multiplier = 3;

    let calculation = {
        let value = 5 + 4;
        value * multiplier
    };
    println!("{calculation}");
}

fn print_string(string: &str) {
    println!("String: {string}");
}

fn square(number: i32) -> i32 {
    return number * number;
}

fn square_implicit(number: i32) -> i32 {
    number * number // No semicolon
}
