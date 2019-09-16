#include <stdio.h>
#include <unistd.h>
int main(int argc, char **argv)
{
    printf("Real user id is %d\n", getuid());
    printf("Effective user id is %d\n", geteuid());
    printf("Real group id is %d\n", getgid());
    printf("Effective group id is %d\n", getegid());
    return 0;
}