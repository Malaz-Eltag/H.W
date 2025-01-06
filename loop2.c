#include <stdio.h>
int main () {  
int u = 0;   
int m = 0;

while ( u < 10 ){
    printf("#" );
    u++; }
    printf("\n");

for (int x=0;x<3;x++) {
            
    printf("#");
      
    for (int y=0;y<8;y++){
            
        printf("*"); }

    printf("#" ); 
    printf("\n"); }

do { 
    printf("#");
    m++;
    }while ( m < 10 );
       
    

    return(0);
}