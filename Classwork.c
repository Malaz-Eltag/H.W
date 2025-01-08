#include <stdio.h>
 int l(int *u){
    (*u) += 3;

 }

 int main() {

int u = 4;
int* o = & u ;
l(o);

printf("%d\n",*o);


int y[5] ={1,2,3,4,5 };
for (int u =0;u<5;u++){
    printf("%d ",y[u]);
printf("");}
printf("\n===================\n");

int r =0;
//while (y[r] != '\0'){
  //  printf("%d ",y[r]);
    //r++;
//}



    return(0);
 }