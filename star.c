#include <stdio.h>
#include <string.h>

//내가 만든 답안
int main(void)
{
    char str[50];
    printf("단어 입력 : ");
    scanf("%s", str);

    printf("입력한 단어 : %s, ", str);
    if (strlen(str) > 5)
    {
        int i;
        for (i=5; i<strlen(str); i++)
        {
            str[i] = '*';
        }
        str[strlen(str)] = '\0';
        printf("생략한 단어 : %s", str);
    }
    else
    {
        printf("생략한 단어 : %s", str);
    }
    return 0;
}

//해설지
int main(void)
{
    char str[80]; //문자열을 입력할 배열
    char res_str[80]; // 생략 문자열을 저장할 배열
    char *star = "*********"; //생략 부분을 채울 문자열
    int len; // 입력 문자열의 길이 보관

    printf("단어 입력 : ");
    scanf("%s", str);
    len = strlen(str);
    if (len <= 5)
    {
        strcpy(res_str, str);
    }
    else
    {
        strncpy(res_str, str, 5); // 다섯 문자만 복사
        res_str[5] = '\0'; // 마지막에 널 문자 저장
        strncat(res_str, star, len - 5); //문자열의 길이만큼 별로 채운다.
    }
    printf("입력한 단어 : %s, 생략한 단어 : %s\n", str, res_str);
    return 0;
}