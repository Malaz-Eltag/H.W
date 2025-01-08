#include <stdio.h>
int First_Name(char First[]) {
    int F = 0;
    while(First[F] != '\0') {
        printf("%c",First[F]);
        F++;
    }
}

int Middle_Name(char Middile[]) {
    int M = 0;
    while(Middile[M] != '\0') {
        printf("%c",Middile[M]);
        M++;
    }
}

int Last_Name(char Last[]) {
    int L = 0;
    while(Last[L] != '\0') {
        printf("%c",Last[L]);
        L++;
    }
}

int Jop(char Jo[]) {
    int J = 0;
    while(Jo[J] != '\0') {
        printf("%c",Jo[J]);
        J++;
    }
}

int main () {
char Name[6] = {'M' , 'a' ,'l', 'a', 'z', '\0'};
char Name_2[15] = "Eltag Mohamed ";
char Name_3[9] = "Abdallah";
int Age = 2;
char Jop_1[8] = {'S','t', 'u', 'd' ,'e', 'n','t' };

printf("Your First Name is : " );
First_Name(Name);
printf("\n");

printf("Your Middle Name is : " );
Middle_Name(Name_2);
printf("\n");

printf("Your Last Name is : " );
Last_Name(Name_3);
printf("\n");

printf("Your Full Name is : ");
First_Name(Name);
printf(" ");
Middle_Name(Name_2);
printf(" ");
Last_Name(Name_3);
printf("\n");

printf("Your Age is : %d%d", Age,Age);
printf("\n");

printf("Your Jop is : " );
Jop(Jop_1);
printf("\n");

    return(0);

}

