import 'dart:io';

void main() {
  var numbers = List.generate(10, (i) => i);
  print("Even num: ${getEvenNumbers(numbers)}");

  greeting();
}

greeting() {
  print("What's your name?");
  var name = stdin.readLineSync();

  if (name.isEmpty) {
    print("You don't have a name");
  } else {
    print("$name, Your are cool");
  }
}

bool isEven(int x) {
  // An if-else statement.
  if (x % 2 == 0) {
    return true;
  } else {
    return false;
  }
}

List<int> getEvenNumbers(Iterable<int> numbers) {
  var evenNumbers = <int>[];

  // A for-in loop.
  for (var i in numbers) {
    // A single-line if statement.
    if (isEven(i)) evenNumbers.add(i);
  }

  return evenNumbers;
}
