fn main() {
    let time = 2025;
    let year = time;

    let text = String::new();
    let text2 = String::from("I am a string");
    println!("{}", text2);

    let mut name = String::from("Boris");
    println!("{name}");
    name.push_str(" Pask");
    println!("{name}");

    let person = String::from("Boris");
    let genius = person;

    let person = String::from("Boris");
    let genius = person.clone();
    println!("{person}, {genius}");

    let my_stack_value = 2;
    let my_integer_reference = &my_stack_value;

    let my_heap_value = String::from("Toyota");
    let my_heap_reference = &my_heap_value;
    println!("{}", *my_heap_reference);
    println!("{}", my_heap_reference);

    let ice_cream = "Cookies and Cream";
    let dessert = ice_cream;

    let oranges = String::from("Oranges");
    print_my_value(oranges);
    // println!("{oranges} is still valid");

    let mut burger = String::from("Burger");
    add_fries(burger);

    let cake = bake_cake();
    println!("I now have a {cake} cake");

    let mut current_meal = String::new();
    add_flour(&mut current_meal);

    show_my_meal(&current_meal);

    let mut car = String::from("Red");
    // let ref1 = &mut car;
    // car.push_str(" car");
    // println!("{ref1}");

    let mut coffee: String = String::from("Mocha");
    let a = &mut coffee;
    println!("{a}");
    let b = a; // b replaces a, a no longer exists
    println!("{b}");

    let city = create_city();
    println!("{city}");

    let registrations = [true, false, true];
    let first = registrations[0];
    println!("{first} and {registrations:?}");

    let languages = [String::from("Rust"), String::from("Python")];
    let first = &languages[0];
    println!("{first} and {languages:?}");
}

fn create_city() -> String {
    let city = String::from("New York");
    city
}

fn show_my_meal(meal: &String) {
    println!("Meal: {meal}");
}

fn add_flour(meal: &mut String) {
    meal.push_str("Add flour");
}

fn bake_cake() -> String {
    let cake = String::from("Chocolate Mousse");
    cake
}

fn add_fries(mut meal: String) {
    meal.push_str(" and fries");
    println!("{meal}");
}

fn print_my_value(value: String) {
    println!("Your value is {value}");
}
