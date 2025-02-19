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
}
