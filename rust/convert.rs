use std::convert::From;
use std::convert::TryFrom;
use std::convert::TryInto;
use std::fmt;

// From
#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

// TryFrom
#[derive(Debug, PartialEq)]
struct EvenNumber(i32);

impl TryFrom<i32> for EvenNumber {
    type Error = ();

    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value % 2 == 0 {
            Ok(EvenNumber(value))
        } else {
            Err(())
        }
    }
}

// ToString
struct Circle {
    radius: i32,
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    // From
    let num = Number::from(30);
    println!("My number is {:?}", num.value);

    // Into
    let int = 5;
    // 试试删除类型说明
    let newnum: Number = int.into();
    println!("My new number is {:?}", newnum);

    // TryFrom
    assert_eq!(EvenNumber::try_from(8), Ok(EvenNumber(8)));
    assert_eq!(EvenNumber::try_from(5), Err(()));

    // TryInto
    let result: Result<EvenNumber, ()> = 8i32.try_into();
    assert_eq!(result, Ok(EvenNumber(8)));
    let result: Result<EvenNumber, ()> = 5i32.try_into();
    assert_eq!(result, Err(()));

    // ToString
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());

    // ToString & FromStr
    let parsed: i32 = "2".parse().unwrap();
    let turbo_parsed = "3".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println! {"Sum: {:?}", sum};
}

// https://rustwiki.org/zh-CN/rust-by-example/conversion/try_from_try_into.html
