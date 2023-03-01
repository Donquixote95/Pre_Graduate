//strcpy 함수의 주의할 점
//1. 첫 번째 인수는 char 배열이나 배열명을 저장한 포인터만 사용할 수 있다.
//2. 두 번째 인수는 문자열의 시작 위치를 알 수 있따면 어떤 것이든 사용할 수 있다.

#include <stdio.h>
#include <string.h>

int main(void)
{
    char str1[80] = "strawberry";
    char str2[80] = "appple";
    char *ps1 = "banana";
    char *ps2 = str2;

    printf("First : %s\n", str1);
    strcpy(str1, str2);
    printf("Change : %s\n", str1);

    strcpy(str1, ps1);
    printf("Change2 : %s\n", str1);

    strcpy(str1, ps2);
    printf("Change3 : %s\n", str1);

    strcpy(str1, "banana");
    printf("Change4 : %s\n", str1);

    return 0;
}