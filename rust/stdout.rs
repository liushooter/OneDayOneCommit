use std::io::{stdout, Write};

fn main() {
    std::io::stdout().write(b"Hi\n").unwrap();
    let mut lock = stdout().lock();
    writeln!(lock, "hello world").unwrap();

    println!("Hello"); // => "Hello"
    println!("Hello, {}!", "world"); // => "Hello, world!"
    println!("The number is {}", 1); // => "The number is 1"
    println!("{:?}", (3, 4)); // => "(3, 4)"
    println!("{value}", value = 4); // => "4"
    let people = "Rustaceans";
    println!("Hello {people}!"); // => "Hello Rustaceans!"
    println!("{} {}", 1, 2); // => "1 2"
    println!("{:04}", 42); // => "0042" with leading zeros
    println!("{:#?}", (100, 200)); // => "(100, 200,)"

    println!("Hello {:5}!", "x");
    println!("Hello {:1$}!", "x", 5);
    println!("Hello {1:0$}!", 5, "x");
    println!("Hello {:width$}!", "x", width = 5);
    let width = 5;
    println!("Hello {:width$}!", "x");

    eprintln!("err"); // printed to the standard error
    eprint!("err");
}
