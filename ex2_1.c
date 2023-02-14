#include <stdio.h> // stdio : standard input ouput(표준입출력)
#include <string.h>

// stdio.h 에는 C언어에서 기본으로 사용하는 입출력 함수가 들어 있다. printf 함수도 포함

int main(void) //function prototype
{
    10+20;

    printf("Be happy\n");
    printf("1234569789\n");
    printf("My\tfriend\n");
    printf("Good\bd\tchance\n");
    printf("Cow\rW\a\n");
    printf("\n");    

    printf("%d\n", 10);
    printf("%lf\n", 3.5); // 소수점 이하 6자리까지 출력된다.
    printf("%.1lf\n", 3.45); //소수점 이하 첫째 자리까지 출력(둘째 자리에서 반올림)
    printf("%.10lf\n", 3.45); //소수점 이하 10자리까지 출력
    printf("\n");

    printf("%d\n", 12); //10진수
    printf("%d\n", 014); //8진수를 10진수로 출력
    printf("%d\n", 0xc); //16진수를 10진수로 출력
    printf("\n");

    printf("%o\n", 12); //8진수로 출력
    printf("%x\n", 12); //16진수 소문자로 출력
    printf("%X\n", 12); //16진수 대문자로 출력
    printf("\n");

    printf("%.1lf\n",1e6); // 지수 형태의 실수를 소수점 형태로 출력
    printf("%.7lf\n",3.14e-5); // 소수점 이하 7자리까지 출력, 기존 출력 방식은 소수점 이하 6자리까지만 출력된다.
    printf("%le\n",0.0000314); // 소수점 형태의 실수를 지수 형태로 출력
    printf("%.2le\n",1e6); // 지수 형태로 소수점 이하 둘째 자리까지 출력
    printf("\n");

    printf("%c\n", 'A'); //문자 상수 출력
    printf("%s\n", "A"); //문자열 상수 출력
    printf("%c은 %s입니다.\n", '1', "first"); // 문자(%c)와 문자열(%s)을 함께 출력

    int a;
    int b,c;
    double da;
    char ch;

    a=10;
    b=a;
    c=a+20;
    da=3.5;
    ch='A';

    printf("변수 a의 값 : %d\n", a);
    printf("변수 b의 값 : %d\n", b);
    printf("변수 c의 값 : %d\n", c);
    printf("변수 da의 값 : %.1f\n", da);
    printf("변수 ch의 값 : %c\n", ch);

    char ch1 = 'A'; //문자로 초기화, 저장된 값은 문자의 아스키 코드 값
    char ch2 = 65; //문자 'A'의 아스키 코드 값에 해당하는 정수로 초기화

    printf("문자 %c의 아스키 코드 값 : %d\n", ch1, ch1);
    printf("아스키 코드 값이 %d인 문자 : %c\n", ch2, ch2);

    short sh = 32767;
    int in = 2147483647;
    long ln = 2147483647;
    long long lln = 123456789;

    printf("short형 변수 출력 : %d\n", sh);
    printf("int형 변수 출력 : %d\n", in);
    printf("long int형 변수 출력 : %ld\n", ln);
    printf("long long int형 변수 출력 : %lld\n", lln);

    printf("char형의 크기 : %d바이트\n", sizeof(char));
    printf("short형의 크기 : %d바이트\n", sizeof(short));
    printf("int형의 크기 : %d바이트\n", sizeof(int));
    printf("long int형의 크기 : %d바이트\n", sizeof(long int));
    printf("long long형의 크기 : %d바이트\n", sizeof(long long));

    //unsigned를 잘못 사용하는 경우
    unsigned int x;

    x = 4294967295; // 큰 양수 저장
    printf("%d\n", x); //%d로 출력, %d는 부호까지 생각해서 10진수로 출력하는 변환 문자
    x = -1;  // 음수 저장
    printf("%u\n", x); //%u로 출력, %u는 부호 없는 10진수로 출력하는 변환 문자

    // 유효 숫자 확인
    float ft = 1.234567890123456789;
    double db = 1.234567890123456789;

    printf("float형 변수의 값 : %.20f\n", ft);
    printf("double형 변수의 값 : %.20lf\n", db);

    char fruit[20] = "strawberry";

    printf("딸기 : %s\n", fruit);
    printf("딸기쨈 : %s %s \n", fruit, "jam");

    // char 배열에 문자열 복사

    char fruits[20] = "strawberry";

    printf("%s\n", fruit);
    strcpy(fruits, "bannaa");
    printf("%s\n", fruits);

// const를 사용하면 초기화된 값을 바꿀 수 없다.
int income = 0;
double tax;
const double tax_rate = 0.12;

income =456;
tax = income * tax_rate;
printf("세금은 : %.1lf입니다.\n", tax);

    return 0;
}

// 제어 문자: 문자는 아니지만 출력 방식에 영향을 주는 문자. 역슬래시(\)와 함께 사용한다.
// \n : new line, 줄 바꿈
// \b : backspace, 한 칸 왼쪽으로 이동
// \t : 8칸 오른쪽으로 이동
// \r : carriage return, 맨 앞으로 이동
// \a : alert, 벨 소리, 벨소리를 낸다

// 정수는 %d, 실수는 %lf(long float)를 사용한다.

//normalization notation ; 정규화 표기법, 소수점 앞에 0이 아닌 유효 숫자 한 자리를 사용하여 지수 형태로 바꾼 것

//문자는 작은따옴표(문자 상수)로 묶고, 문자열은 큰따옴표(문자열 상수)로 묶는다. 하나의 문자라도 큰따옴표가 붙으면 문자열 상수다.

//float형은 유효 숫자 7자리, double형은 15자리의 범위 내의 값을 사용하는 게 좋다.
//long double형의 크기는 컴파일러마다 다르다. 유닉스나 리눅스에서 사용하는 gcc 컴파일러는 16바이트, VC++ 컴파일러는 double형과 같은 8바이트로 처리한다.
//long duble의 출력 변환 문자는 %Lf
//Dev-C++ 컴파일러는 12바이트, TC++ 컴파일러는 10바이트로 처리한다.
//실수는 double형 변수에 저장하는 게 안전하고, 꼭 float형 변수를 사용한다면 저장할 값도 1.23f(또는 1.23F)와 같이 f,F를 붙여서 4바이트 크기의 상수로 처리되도록 작성하는 게 좋다.

/*
char 배열명[문자열 길이 + 1] = 문자열;
 - 문자열의 길이보다 배열의 크기를 하나 더 크게 잡아야 하는 이유는 컴파일러가 문자열의 끝에
 - \0(null character)을 자동으로 추가하기 때문이다. 널 문자는 문자열의 끝을 표시하는 특별한 문자다.

예를 들면, apple을 저장하려면
char fruit[6] = "apple";
*/

//strcpy ; string copy 함수

// reserved word(예약어) ; 컴파일러와 사용 방법이 약속된 단어
// identifier(식별자) ; 필요에 따라 만들어 사용하는 단어