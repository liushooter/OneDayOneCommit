#include <stdio.h>

#define MAXLINE 1000

int my_getline(char line[], int maxline);
void copy(char to[], char from[]);

/*
  getline 是标准库函数
 */

main(){
  int len;  // 当前行长度
  int max; // 目前为止发现的最长行的长度
  char line[MAXLINE]; // 当前输入行
  char longest[MAXLINE]; // 用于保存最长的行

  max = 0;
  while((len = my_getline(line, MAXLINE)) > 0){
    if (len > max){
      max = len;
      copy(longest, line);
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
int my_getline(char s[], int lim){
  int c,i;

  for (int i = 0; i < lim-1 && ((c = getchar()) != EOF && c != '\n' ); ++i){
      s[i] = c;
  }

  if (c == '\n'){
    s[i] = c;
    ++i;
  }
  s[i] = '/0';

  return i;
}


/*
  将 from 复制到to,这里指定to足够大
*/
void copy(char to[], char from[]){
  int i;
  i = 0;

  while( (to[i] = from[i]) != '\0'){
    ++i;
  }
}