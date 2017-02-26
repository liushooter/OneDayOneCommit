#include <stdlib.h>
#include <stdio.h>

void f1(void){
  puts("pushed first"); //stdio
}

void f2(void){
  puts("pushed second");
}

int main(void)
{
  atexit(f1); // stdlib
  atexit(f2);
}

// http://zh.cppreference.com/w/c/program/atexit