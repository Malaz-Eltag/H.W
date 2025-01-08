#include <stdio.h>
int Name(char str[])
 { int u=0;
 while (str[u]!= '\0'){
printf("%c",str[u]);
u++;
 }
    printf("\n");

 }


int main() {
    char my[] = "malaz eltag";
   printf("Your First Name is: ");
   Name(my);

/*char u[12] ;
printf("Enter Your Name :");
scanf("%s",u);
printf("Your Name is: %s\n",u);


char Name[15];
printf("Enter Your Name :");
fgets( Name ,sizeof(Name),stdin );
//printf("\n");
printf("Your Name is: %s", Name);
printf("Hello, %s", Name);
//printf("\n");*/

    return(0);
}