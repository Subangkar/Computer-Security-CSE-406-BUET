#include <unistd.h>
#include <stdio.h>

void f1(){
    printf("f1\n");
}

void f2(){
    printf("f2\n");
}


int main(int argc, char const *argv[])
{
    char buf[124];
    execv("/bin/sh", NULL);
    return 0;
}


