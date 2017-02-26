#include <stdio.h>

int main(){
  int c, nl;
  nl = 0;
  while((c = getchar()) != EOF){
    if(c == '\n'){
      ++nl;
    }
  }

  printf("\n----- Ctrl+d -----\n");
  printf("line is %.0f \n", nl);
}