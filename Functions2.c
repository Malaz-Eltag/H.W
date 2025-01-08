#include <stdio.h>
int First_Name(char *First) {
    while(*First != '\0') {
        printf("%c",*First);
        First++;
    }
}

int Middle_Name(char *Middle) {
    while(*Middle != '\0') {
        printf("%c",*Middle);
        Middle++;
    }
}

int Last_Name(char *Last) {
    while(*Last!= '\0') {
        printf("%c",*Last);
        Last++;
    }
}

int Jop(char *Jo) {
    while(*Jo != '\0') {
        printf("%c",*Jo);
        Jo++;
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

