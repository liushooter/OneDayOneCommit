#include <iostream>
using namespace std;

typedef struct {
  int x;
  int y;
}Coord; // 坐标


int main(void) {
  Coord c1;
  Coord &c = c1;
  c.x = 521;
  c.y = 520;
  int a = 3;
  int &b = a; // 引用必须初始化
  b = 10;
  cout << a << endl;
  cout << c1.x << " " << c1.y << endl;
  return  0;
}