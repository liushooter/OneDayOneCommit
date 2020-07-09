/*
  * 注释
  * 注释
  * 注释
*/
void main() {
  // 必须有main函数作为入口

  var hi = "hi"; // 普通变量
  String language = "dart";

  print(hi + " " + language);
  personage();
  checkBitLength();
}

void personage() {
  const name = "liu"; // 常量
  Object midName = 'Nicholas';
  dynamic lastName = '能';
  final extraName = "Plus"; // 常量

  print("$name $midName $lastName $extraName");
  how();
}

void how() {
  const int speed = 100; // 速度
  const double distance = 2.5 * speed; // 距离 隐式转换

  print("is driving, speed: $speed, distance: $distance");
}

checkBitLength() {
  int a1 = 1;
  int a2 = 12;
  int a3 = 123;
  int a4 = 1234;
  print('${a1.bitLength}'); // 1个bit  相当于二进制数字 00000000 00000001
  print('${a2.bitLength}'); // 4个bit  相当于二进制数字 00000000 00001100
  print('${a3.bitLength}'); // 7个bit  相当于二进制数字 00000000 01111011
  print('${a4.bitLength}'); // 11个bit 相当于二进制数字 00000100 11010010
}
