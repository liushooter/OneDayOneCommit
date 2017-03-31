//内存管理
#include <iostream>
using namespace std;
int main(void)
{

  int *p = new int; //申请
  delete p; //释放
  p = nullptr; //空指针


  int *arr = new int(10); // 申请块内存  不是int[10]
  int *zqw = new int[20]; // 申请块内存  不是int[10]

  cout << arr << "----" << zqw;

  if (arr == nullptr){
    cout << "申请失败";
    // 重复释放也会出问题
  } else {
    cout << *arr << endl;

    delete  []arr; // 释放块内存
    arr = nullptr;
    cout << "申请成功 释放成功" << endl;
  }


  return 0;
}