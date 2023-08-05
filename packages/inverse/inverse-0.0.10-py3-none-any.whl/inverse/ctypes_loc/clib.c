#include <stdio.h>
// gcc -fPIC -shared -o clibSHARED.so clib.c

char *display(char *str, int age)
{
    printf("my name is %s  and age is %d", str, age);
    return "completed";
}


int main(void)
{

    return 0;
}