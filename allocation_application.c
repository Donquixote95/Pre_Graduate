#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//main 함수의 명령행 인수 사용
//명령행 인수(command line argument) ; 명령행에서 프로그램을 실행시킬 때는 프로그램의 이름 외에도 프로그램에 필요한 정보를 함께 줄 수 있다. 이들을 모두 명령행 인수라고 한다.
// 운영체제가 명령행 인수를 프로그램의 main 함수로 넘기는 방법을 통해 포인터로 동적 할당한 영역을 배열처럼 사용하는 예를 살펴보자.
int main(int argc, char **argv) //명령행 인수를 받을 매개변수
//매개변수의 이름은 임의로 작성할 수 있다. 그러나 관례적으로 argc와 argv를 사용한다.
//의미는 argument count, argument verctor이다.
/*
명령행 인수의 개수 3은 argc 매개변수에 저장되고(왜 3인지는 p470 참조),
명령행에서 입력한 문자열의 위치는 argv 매개변수에 저장된다.
*/
{
    int i;

    for(i = 0; i < argc; i++) //인수 개수 만큼 반복
    {
        printf("%s\n", argv[i]);
    }
    
    return 0;
}

// void print_str(char **ps); // 동적 할당 영역의 문자열을 출력하는 함수

// int main(void)
// {
//     char temp[80]; // 임시 char 배열
//     char *str[21] = { 0 }; // 문자열을 연결할 포인터 배열, 널 포인터로 초기화, 22개의 공간이 모두 널로 초기화 된다.
//     int i = 0;

//     while (i < 20) // 최대 20개까지 입력한다. 20개를 다 채우면, str[20] 즉, 21번째는 최소 NULL 포인터를 저장해야 한다..?
//     {
//         printf("문자열을 입력하세요 : ");
//         gets(temp); // 문자열 입력
//         if (strcmp(temp, "end") == 0) break; //end가 입력되면 반복 종료
//         //strcmp() 함수는 2개의 string을 비교하는 함수다.
//         //같으면 0을 리턴
//         str[i] = (char *)malloc(strlen(temp) + 1); // 문자열 저장 공간 할당, null 값도 포함해서
//         strcpy(str[i], temp);
//         i++;
//     }
//     print_str(str);

//     for (i = 0; str[i] != NULL; i++) // str에 연결된 문자열이 없을 때까지
//     {
//         free(str[i]); // 동적 할당 영역 반환
//     }

//     return 0;
// }

// void print_str(char **ps)
// {
//     while (*ps != NULL) // 배열의 포인터가 널 포인터가 아닌 동안 반복
//     {
//         printf("%s\n", *ps); // ps가 가리키는 것은 포인터 배열 요소
//         ps++; //ps가 다음 배열 요소를 가리킨다.
//     }
// }


// int main(void)
// {
//     char temp[80];
//     char *str[3];
//     int i;

//     for ( i= 0; i < 3; i++)
//     {
//         printf("문자열을 입력하세요 : ");
//         gets(temp);
//         str[i] = (char *)malloc(strlen(temp) + 1);
//         strcpy(str[i], temp);
//     }

//     for (i = 0; i < 3; i++)
//     {
//         printf("%s\n", str[i]);
//     }

//     for (i = 0; i < 3; i++)
//     {
//         free(str[i]);
//     }

//     return 0; 
// }