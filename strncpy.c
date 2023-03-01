//원하는 개수의 문자만을 복사하는 strncpy 함수

#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[20] = "mango tree";

    strncpy(str, "apple-pie", 5);
    str[5] = '\0';

    printf("%s\n", str);

    return 0;
}