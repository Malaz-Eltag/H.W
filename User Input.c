#include <stdio.h>
int main() {
/*char u[12] ;
printf("Enter Your Name :");
scanf("%s",u);
printf("Your Name is: %s\n",u);
*/

char Name[15];
int Age;
int c;
printf("Enter Your Name :");
fgets( Name ,sizeof(Name),stdin );
/*while(Name!=  ) {
    printf(" please Enter Number !");
    return(1);
}
*/
for(c;c < 15;c++){
    
printf(" ");
}
//printf("\n");
printf("Enter Your Age :" );
scanf("%d" ,&Age);
while(Age !=  ) {
    printf(" please Enter string !");
    return(1);
}

printf("Your Name is: %sand Your Age is: %d ",Name,Age );
//printf("Hello, %s", Name);
//printf("\n");


    return(0);
}