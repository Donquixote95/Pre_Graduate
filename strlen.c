#include <stdio.h>

char *my_strcpy(char *pd, char *ps);
char *my_strcat(char *pd, char *ps);
int my_strlen(char *ps);
int my_strcmp(char *pa, char *pb);

int main(void)
{
    char str[80] = "strawberry";

    printf("Before change : %s\n", str);
    my_strcpy(str, "apple");
    printf("After change : %s\n", str);
    printf("Assignment : %s\n", my_strcpy(str, "kiwi"));
    printf("my_strlen : %d\n", my_strlen("Great!"));
    printf("my_strcmp : %d\n", my_strcmp("apple", "great!"));

    return 0;
}

char *my_strcpy(char *pd, char *ps) // 복사 받을 곳(pd), 복사할 곳(ps)의 포인터
{
    char *po = pd; //pd 값을 나중에 반환받기 위해 보관

    while (*ps != '\0')
    {
        *pd = *ps;
        pd++;
        ps++;
    }
    *pd = '\0'; //복사가 모두 끝나면 널 문자로 마무리

    return po;
}

char *my_strcat(char *pd, char *ps)
{
    char *po = pd;

    while (*pd != '\0')
    {
        pd++;
    }
    while (*ps != '\0')
    {
        *pd = *ps;
        pd++;
        ps++;
    }
    *pd = '\0';
    return po;
}

int my_strlen(char *ps)
{
    int cnt = 0;
    while (*ps != '\0')
    {
        cnt++;
        ps++;
    }
    return cnt;
}

int my_strcmp(char *pa, char *pb)
{
    while ((*pa == *pb) && (*pa != '\0'))
    {
        pa++;
        pb++;
    }

    if (*pa > *pb)
    {
        return 1;
    }
    else if (*pa < *pb)
    {
        return -1;
    }
    else
    {
        return 0;
    }
}


// #include <stdio.h>
// #include <string.h>

//strcmp, strncmp 문자열 비교
//strcpm 두 문자열의 사전 순서를 판단하여 결과를 반환한다. 사전 순서는 사전에 단어가 수록되는 알파벳 순서를 말한다.
//strcmp(str1, str2); 
//str1이 str2보다 사전에 나중에 나오면 1 반환, 반대면 -1 반환, 같으면 0 반환

//strncmp() 함수는 비교할 문자 수를 세 번째 인수로 지정할 수 있다.
// int main(void)
// {
//     char str1[80] = "pear";
//     char str2[80] = "peach";

//     printf("precedence : ");
//     if (strcmp(str1,str2)>0)
//     {
//         printf("%s\n", str1);
//     }
//     else
//     {
//         printf("%s\n", str2);
//     }

//     printf("Compare with 3 charaters :\n ");
//     if (strncmp(str1, str2, 3) == 0)
//     {
//         printf("same\n");
//     }
//     else
//     {
//         printf("different\n");
//     }

// }

// strlen 함수
// int main(void)
// {
//     char str1[80], str2[80];
//     char *resp;

//     printf("Two fruits : ");
//     scanf("%s%s", str1, str2);
//     if (strlen(str1) > strlen(str2))
//         {
//             resp = str1;
//         }
//     else
//         {
//             resp = str2;
//         }
//     printf("The fruit which has a longer name : %s", resp);

//     return 0;
// }