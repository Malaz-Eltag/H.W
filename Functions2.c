#include <stdio.h> 

char First_Name[6] = {'M' , 'a' ,'l', 'a', 'z', '\0'};
char *First = First_Name;
char Middle_Name[13] = "Eltag Mohamed";
char *Middle = Middle_Name;
char Last_Name[9] = "Abdallah";
char *Last = Last_Name;
int Age[2] = {2,'\0' };
int *a = Age;
char Jop[8] = {'S','t', 'u', 'd' ,'e', 'n','t' };
char *j = Jop;
int u ,w,s,i =0 ;
int main () {
printf("Your First Name is: ");
for( u =0; u < 6 ; u++){
    printf("%c", *First); 
    First++;}

printf("\n");
printf("Your Middle Name is :");
for( w =0; w < 13 ; w++){
    printf("%c",*Middle);
    Middle++;}
printf("\n");
printf("Your Last Name is :");
for(s = 0; s < 8 ; s++){
    printf("%c",*Last);
    Last++;}

printf("\n");
printf("Your Name :%s %s",First_Name,Last_Name);
printf("\n"); 
printf("Your Full Name is :%s %s %s",First_Name,Middle_Name,Last_Name);


printf("\n"); 
printf("Your Age is :%d%d", *a ,*a);
printf("\n");
printf("Your Job is : ");
for( i =0; i < 7 ; i++){
    printf("%c",*j); 
    j++; }

}