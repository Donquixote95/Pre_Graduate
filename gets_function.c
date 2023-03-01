//gets 함수 구현
#include <stdio.h>
void my_gets(char *ps);

int main(void)
{
    int i = 0;
    char str[20];
    char ch;

    //my_gets(str);

    do
    {
        ch = getchar();
        str[i] = ch;
        i++;
    } while (ch != '\n');
    
    str[--i] = '\0'; // 개행 문자가 입력된 위치에 널 문자 저장
    printf("%s", str);
    return 0;
}

void my_gets(char *ps)
{
    char ch;

    while ((ch = getchar()) != '\n')
    {
        *ps = ch;
        ps++;
    }
    *ps = '\0';
}