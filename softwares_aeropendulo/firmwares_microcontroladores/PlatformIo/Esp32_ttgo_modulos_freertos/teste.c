#include <string.h>
#include <stdio.h>

int main(void){
  void testeVar(int x);
  void testePt(int *px);

  int teste = 1;
  int *pteste = &teste;
  
  testeVar(teste);
  testePt(pteste);
  testePt(pteste);

  printf("%i\n", teste);
  printf("%p\n", &teste);
  printf("%p\n", pteste);
  printf("%p\n", &pteste);
  printf("%i\n", *pteste);

  return 0;
}

void testeVar(int x){
  ++x;
}

void testePt(int *px){
  ++*px;
}
