//Calculator Project 

#include<stdio.h>

int Add(int first, int second )
{
    int result = first + second  ;
    return result ;
    }
int sub(int first , int second )
{
    int result2 = first - second ;
    return result2 ;
    }

int Mult(int first , int second  )
{
    int result3 = first  * second ;
    return result3 ;
    }

int Div(int first , int second )
{
    int result4 = first / second  ;
    return result4 ;
    }

int main () {
int first,secound,result, r, n,w;

char name [20] ,op;

printf("Enter your name: ");
scanf("%s",&name);
for (n = 0; n < 20; n++) {
        if (name[n] >= '0' && name[n] <= '9') {
            printf("wrong value, please enter a character\n");
            return(1); }  }
        if ( n > 19 ) {
        printf(" Greeting, %s \n", name); }


printf("Enter the calculationas as A + B \n");

scanf("%d %c %d",&first,&op,&secound);

int Add1= Add(first, secound);
int sub1 = sub(first, secound);
int Mult1  = Mult(first, secound);
int Div1 = Div(first, secound);
     
switch (op) {
    case '+':
    result = Add1 ;
    break;
    case '-':
    result = sub1 ;
    break;
    case '*':
    result = Mult1 ;
    break;
    case '/':
    result = Div1 ;
    break;
    default:
    printf(" Wrong entry please try again\n");
    return(1);
    }


printf("%d %c %d = %d",first ,op,secound,result );

    return(0);
}
