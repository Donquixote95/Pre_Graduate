//문자열을 붙이는 함수
//strcat ; 문자열을 이어 붙인다
//strncat ; 지정한 문자의 개수만큼 붙인다.

//주의할 점
/*
1. 메모리를 침범할 수 있다.
2. strcat 함수를 사용할 때는 배열을 초기화해야 한다.
*/

#include <string.h>
#include <stdio.h> 

int main(void)
{
    char str[80] = "straw";
    //초기화하는 4가지 방법
    char str1[80] = {'\0'}; //명시적으로 널 문자를 초기화
    char str2[80] = {0}; //null charater의 ASCII 코드 값으로 초기화
    char stt3[80] = ""; //큰따옴표 안에 아무것도 없으므로 널 문자만 초기화
    char stt4[0] = '\0' //첫 번째 배열 요소만 별도로 초기화
    strcat(str, "berry");
    printf("%s\n", str);
    strncat(str, "piece", 3);
    printf("%s\n", str);

    return 0;
}