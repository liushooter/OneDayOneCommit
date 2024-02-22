use std::ops::Deref;
use std::ops::DerefMut;

struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

// 将一个可变引用转换成另一个可变引用
impl<T> DerefMut for MyBox<T> {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.0
    }
}

fn display(_str: &str) {
    println!("display value: {}", _str)
}

fn hi(s: &mut String) {
    s.push_str(" world");
    println!("{}", s);
}

fn main() {
    let x = Box::new(1);
    let sum = *x + 1;
    println!("sum is: {}", sum);

    // String 实现了 Deref<Target=str>
    let s = MyBox::new(String::from("rust"));

    let mut mut_str = MyBox::new(String::from("rust"));

    display(&s);

    hi(&mut mut_str);

    let y = MyBox::new(5);

    assert_eq!(5, *y, "ok");
    assert_eq!(6, *y, " not equal")
}

// https://course.rs/advance/smart-pointer/deref.html
// https://rustwiki.org/zh-CN/book/ch15-00-smart-pointers.html
