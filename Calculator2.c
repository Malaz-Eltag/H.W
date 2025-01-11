
//Calculator Project 

#include <stdio.h>
int Add(float First_Number[10], float Second_Number[10] )
{
    float result = First_Number[10]+ Second_Number[10] ;
    return result ;
    }
int sub(float First_Number[10], float Second_Number[10] )
{
    float result2 = First_Number[10] - Second_Number[10] ;
    return result2 ;
    }

int Mult(float First_Number[10], float Second_Number[10] )
{
    float result3 = First_Number[10] * Second_Number[10] ;
    return result3 ;
    }

int Div(float First_Number[10], float Second_Number[10] )
{
    float result4 = First_Number[10] / Second_Number[10] ;
    return result4 ;
    }


int main(){

char Name[50] ;
float First_Number[10];
float Second_Number[10];
int s; 
int u ,v;
char choice ;
float num[12] = {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0};


printf("Enter your name( Just character ): ");
fgets(Name,sizeof(Name),stdin);
for (u = 0; u < 50; u++) {
        if (Name[u] >= '0' && Name[u] <= '9') {
            printf("wrong value, please enter a character\n");
            return(1);
        }
    }
 if (u > 49) {
printf(" Greeting ,%s",Name); }        


printf("Please Entar First Number : ");
 scanf("%f",&First_Number[10]);

for (s = 0; s < 10 ; s++) {
    
        if (  First_Number[10] < num[12] )   { 
        
            printf("wrong value, please enter a Integer \n");

            return(1);
            }

       else {
        
             printf("");

            }
            }   
        if  (s > 9) {
            printf(" ");
            
        }


printf("Select a calculation : + , - , /, * \n "); 

scanf(" %c",&choice);

if (choice == '+' || choice == '/' || choice == '-' || choice == '*' ) {
    printf("");
     }
else {
    printf("\nWrong choice , please select a valid choice \n");
    return(1);}

printf("\nPlease Entar Second Number : ");
scanf("%f",&Second_Number[10]);

for (v = 0; v < 10 ; v++) {
    if (Second_Number[10] < num[12] ) {
        //printf(" ");
    
        printf("\nwrong value, please enter a Integer \n");
            return(1);
    
    }

    else {
        printf(""); 
    }
    }
    

float Add1 = Add(First_Number, Second_Number);
float sub1 = sub(First_Number, Second_Number);
float Mult1  = Mult(First_Number, Second_Number);
float Div1 = Div(First_Number, Second_Number);


if ( choice == '+') { 
printf("Your equation is : \n%.2f %c %.2f ",First_Number[10],choice,Second_Number[10]);
printf("\nThe result is : %.2f ",Add1); }


else if ( choice == '-') { 
printf("Your equation is : \n%.2f %c %.2f " ,First_Number[10],choice,Second_Number[10]); 
printf("\nThe result is : %.2f ",sub1);}


else if ( choice == '/')   {
    printf("Your equation is : \n%.2f %c %.2f ",First_Number[10],choice,Second_Number[10]);
    printf("\nThe result is : %.2f ",Div1); }

else if (choice == '*') {
    printf("Your equation is : \n%.2f %c %.2f ",First_Number[10],choice,Second_Number[10] );
    printf("\nThe result is : %.2f ",Mult1); }

else {printf("Invalid input"); }

    return (0);
}