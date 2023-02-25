#include <stdio.h>

//getchar 함수와 putchar함수
//scanf 함수는 문자뿐만 아니라 숫자도 입력하는 기능이 포함되어 있으므로 문자만 입력하는 함수에 비해 크기가 크다.
//printf 함수도 마찬가지
//따라서 문자만 I/O하는 경우에 문자 전용 함수를 쓰는 것이 효율적이다. prototype은 아래와 같다.

int getchar(void);
int putchar(int);

int main(void)
{
    int ch;

    printf("Input : ");
    ch = getchar();

    //getchar 함수는 white space를 입력받는데 이들 문자를 제외하는 option은 없다.

    putchar(ch);
    putchar('\n');

    //putchar 함수는 문자 상수나 문자의 아스키 코드 값을 인수로 주면 해당 문자를 화면에 출력한다.
    //출력한 문자를 다시 반환하며 출력 과정에서 에러가 발생하면 -1을 반환한다.
}

//scanf 함수를 이용한 문자 입력
//white space ; SPaceBar Tab Enter
//%c는 문자를 입력하므로 화이트 스페이스도 입력 대상이 된다.
// int main(void)
// {
//     char ch1, ch2;

//     scanf(" %c %c", &ch1, &ch2); // %c 앞에 화이트 스페이스를 사용하면 입력 문자 중 화이트 스페이스를 무시하고 그 외의 문자만 입력한다.
//     printf("[%c%c]", ch1, ch2);
//     printf("[%d%d]", ch1, ch2);

//     return 0;

    //scanf 함수로 문자를 입력할 때 주의할 점
    //scanf 함수는 입력한 문자를 메모리의 1바이트 공간에 저장하도록 설계되었으므로 int형 변수를 사용하면 나머지 3바이트에 있는
    //garbage value 때문에 입력한 문자의 아스키 코드 값을 사용할 수 없다. 이 경우 입력한 int형 변수를 별도의 char형 변수에 대입하여
    //입력한 문자만을 사용하도록 해야 하는데 {'(char) int형 변수' 처럼 하던지..} 결국 문자를 입력하는 경우에는 char형 변수를 사용하는 것이 좋다.
// }

// int main(void)
// {
//     char small, cap = 'G';

//     if ((cap >= 'A') && (cap <= 'Z'))
//     {
//         small = cap + ('a' - 'A');
//     }
//     printf("Capital : %c %c", cap, '\n');
//     printf("small : %c", small);

//     return 0;
// }