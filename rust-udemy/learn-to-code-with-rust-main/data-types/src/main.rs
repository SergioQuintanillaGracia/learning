fn main() {
    // We can transform a type to i8, for example, by adding `i8`
    // to the end of the number
    // However, it's better to use `: i8` instead
    let i8_value = 20i8;

    let days: usize = 55;
    let years: isize = -15_000;

    let filepath = r"C:\Documents\new\videos";
    println!("{filepath}");

    let value: i32 = -15;

    let empty_space = "       my content     ";
    println!("{}", empty_space.trim());

    println!("{}", value.pow(2));

    let pi: f64 = 3.1415926535897932384;
    println!("The current value of pi is {pi}");
    println!("{}", pi.floor());
    println!("{}", pi.ceil());
    println!("{}", pi.round());

    println!("The current value of pi is {pi:.2}");
    println!("The current value of pi is {:.2}", pi);

    let miles_away = 127;
    let miles_away_i8 = miles_away as i8;
    println!("{}", miles_away_i8);

    let miles_away = 128;
    // Value will overflow and wrap around to -128
    let miles_away_i8 = miles_away as i8;
    println!("{miles_away_i8}");

    let miles_away = 256;
    // Value will overflow and wrap around to 0
    let miles_away_u8 = miles_away as u8;
    println!("{}", miles_away_u8);

    let miles_away = 100.329032;
    let miles_away_int = miles_away as i32;
    println!("{miles_away_int}");

    println!("Floor division: {}", 5 / 3);
    println!("Decimal division: {}", 5.0 / 3.0);

    let age: i32 = -50;
    println!(
        "Positive: {}  |  Negative: {}",
        age.is_positive(),
        age.is_negative()
    );

    println!("{}", "Text" == "Text");
    println!("{}", 13 == 13.0 as i8);

    let first_initial = 'B';
    let emoji = '🦀';
    println!(
        "{} {}",
        first_initial.is_alphabetic(),
        emoji.is_alphabetic()
    );

    println!("{} {}", first_initial.is_uppercase(), emoji.is_uppercase());

    let numbers: [i32; 6] = [4, 8, 15, 16, 23, 42];
    let apples = ["Granny", "McIntosh"];
    println!("Length: {}", apples.len());

    let mut seasons = ["Spring", "Summer", "Fall", "Winter"];
    seasons[2] = "Autumn";
    println!("Second season: {}", seasons[2]);

    println!("{:?}", seasons);
    println!("{seasons:?}");
    println!("{seasons:#?}");

    dbg!(seasons);
    dbg!(2 + seasons.len());

    let employee = ("Molly", 32, "Marketing");
    // let name = employee.0;
    // let age = employee.1;
    // let department = employee.2;

    let (name, age, department) = employee;

    println!("Name: {name}, Age: {age}, Department: {department}");

    dbg!(employee);
}
