//문자열을 출력하는 puts, fputs 함수
// int puts(const char *str); // 문자열을 추력하고 자동 줄 바꿈
// int fputs(const char *str, FILE *stream) // 문자열ㅇ르 출력하고 줄 바꾸지 않음
// puts와 fputs 함수 모두 정상 출력된 경우 0을 반환하고 출력에 실패하면 -1(EOF)을 반환한다.

#include <stdio.h>

int main(void)
{
    char str[80] = "apple juice"; // 배열에 문자열 초기화
    char *ps = "bannna"; //포인터에 문자열 연결

    puts(str);
    fputs(ps, stdout);
    puts("milk");

    return 0;
}

//표준 입력 함수의 버퍼 공유 문제
// #include <stdio.h>

// int main(void)
// {
//     int age;
//     char name[20];

//     printf("age : ");
//     scanf("%d", &age);
//     fgetc(stdin); //버퍼에서 하나의 문자를 읽어서 반환, 반환 문자는 버림
    //scanf("%*c"); //scanf 함수에서 *란 입력을 받되 버리라는 뜻이다.
    //getchar();

//     printf("name : ");
//     gets(name);
//     printf("age : %d, name : %s\n", age, name);

//     return 0;
// }

//fgets 함수를 사용한 문자열 출력 ; 최대 배열의 크기까지만 문자열을 입력한다.
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
// char str[80];
// printf("white space : ");
// fgets(str, sizeof(str), stdin); // 배열명, 배열의 크기, 표준 입력 버퍼(stdin)
//배열의 크기 -1개의 문자를 저장한다. 문자열의 끝에는 항상 널 문자를 붙이기 때문에.
//stdin ; 데이터를 입력할 때 키보드와 연결된 표준 입력 버퍼를 사용하라는 뜻이다.
//scanf gets 함수는 기본적으로 표준 입력을 사용하지만 fgets 함수는 입력 버퍼를 선택할 수 있는 함수다.
//개행 문자의 처리 방식이 다르다.
//Enter를 누를 때 \n이 버퍼에 저장되고, 다른 출력함수는 버퍼의 \n(개행문자)를 -> \0(널 문자)로 배열에 바꿔서 저장한다.
//그러나 fgets 함수는 개행문자\n도 배열에 저장하고, 개행문자 뒤에 널 문자(\0)도 붙여서 배열에 저장한다.
//그래서 출력되고 줄이 바뀐다.

//개행 문자를 제거하려면 str[strlen(str) -1] = '\0'을 이용한다.
//index는 0부터 시작하므로 indexing을 할 때는 전체 문자 수에서 -1을 해야 개행문자가 저장된 곳의 위치가 나온다.
//strlen() 함수는 배열명을 인수로 받아서 널 문자 이전까지의 문자 수를 세어 return한다.
//string.h 헤더 파일을 include 한다.

// str[strlen(str) -1] = '\0';

// printf("Input : %s", str);

// return 0;
// }

//gets 함수를 사용한 문자열 출력
//gets 함수는 중간의 공백이나 탭 문자를 포함하여 문자열 한 줄을 입력한다.
// #include <stdio.h>

// int main(void)
// {
//     char str[80];

//     printf("white spcae : ");
//     gets(str);
//     printf("Input : %s", str);

//     return 0;
// }


// char 포인터로 문자열 사용
// #include <stdio.h>

//scanf 함수를 사용한 문자열 입력
//scanf 함수는 white space가 없는 연속 문자열만 입력받는다.
//배열에 문자열을 저장할 때는 끝에 널 문자를 자동으로 붙인다. 공백 문자 이전까지만 저장한다.
//공백 문자는 자동으로 널 문자를 붙인다.

// int main(void)
// {
//     char str[80];

//     printf("Input charater : ");
//     scanf("%s", str);
//     printf("The first word : %s\n", str);
//     scanf("%s", str);
//     printf("The second word in buffer : %s\n", str);
//     scanf("%s", str);
//     printf("The Third word in buffer : %s\n", str);

//     return 0;
// }

// int main(void)
// {
//     char *dessert = "apple"; //문자열은 주소이기 때문에 가능

//     printf("dessert : %s\n", dessert);
//     //while (*deseert != '\0')
//     //{
//     //     putchar(*dessert);
//     //     dessert++;
//     //}
//     dessert = "banana";
//     printf("Tomorrow dessert : %s\n", dessert);

//     return 0;
// }


// #include <stdio.h>

// int main(void)
// {
//     printf("An first adress of apple : %p\n", "apple");
//     printf("An second adress of second charater : %p\n", "apple" + 1);
//     printf("First charater : %c\n", *"apple");
//     printf("Second charater : %c\n", *("apple"+1));
//     printf("A form of array - Third charater : %c\n", "apple"[2]);

//     return 0;
// }