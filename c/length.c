#include <stdio.h>
#include <string.h>



int main (){
  char *name = "shooter";

  printf("int sizeof is %zu\n", sizeof(int));
  printf("long sizeof is %zu\n", sizeof(long));
  printf("double sizeof is %zu\n", sizeof(double));
  printf("unsigned sizeof is %zu\n", sizeof(unsigned));
  printf("signed sizeof is %zu\n", sizeof(signed));
  printf("short sizeof is %zu\n", sizeof(short));
  printf("char sizeof is %zu\n", sizeof(char));
  printf("const sizeof is %zu\n", sizeof(const));
  printf("_Bool sizeof is %zu\n", sizeof(_Bool)); //没有 bool

  printf("name length is %d\n", strlen(name));
  printf("zqw name length is %d\n", strlen("zqw"));

  return 0;
}