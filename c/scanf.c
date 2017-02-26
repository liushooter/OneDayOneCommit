#include <stdio.h>

int main(void){ // 返回空 void 不是变量(好像)
  int a, b, c;
  printf("input a,b,c\n");
  scanf("%d%d%d", &a, &b, &c);
  printf("a=%d,b=%d,c=%d",a , b, c);
  return 0;
}