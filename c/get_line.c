#include <stdio.h>

#define MAXLINE 1000
int max; // 目前为止发现的最长行的长度
char line[MAXLINE]; // 当前输入行
char longest[MAXLINE]; // 用于保存最长的行

int my_getline(void);
void copy(void);

/*
  getline 是标准库函数
 */

main(){
  int len;  // 当前行长度
  extern int max;
  extern char longest[];

  max = 0;
  while((len = my_getline()) > 0){
    if (len > max){
      max = len;
      copy();
    }
  }

  if (max > 0){ // 存在这样的行
    printf("%s\n",  longest);
  }

  return  0;
}

/*
  将一行读入到s中并返回其长度
*/
int my_getline(void){
  int c,i;
  extern char line[];

  for (int i = 0; i < MAXLINE-1 && ((c = getchar()) != EOF && c != '\n' ); ++i){
      line[i] = c;
  }

  if (c == '\n'){
    line[i] = c;
    ++i;
  }
  line[i] = '/0';

  return i;
}


/*
  将 from 复制到to,这里指定to足够大
*/
void copy(){
  int i;
  extern char line[], longest[];

  i = 0;
  while( (longest[i] = line[i]) != '\0'){
    ++i;
  }
}