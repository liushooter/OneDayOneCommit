// 指针
#include <iostream>
using namespace std;

void func(int &x, int &y);


int main(void)
{
  int a  = 5;
  int *p = &a;  // 指针p指向a
  int *&q = p; // 给p起别名q
  *q = 8;

  int x = 10;
  int y = 20;
  cout << x << "," << y << endl;
  func(x,y);
  cout << x << "," << y << endl;


  cout << &a << endl;
  cout << q << endl;
  cout << *q << endl;
  cout << a << endl;

  return 0;
}

void func(int &a, int &b){
  int c = 0;
  c = a;
  a = b;
  b = c;
}
