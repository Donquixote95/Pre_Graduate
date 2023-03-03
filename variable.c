#include <stdio.h>

void func(void);

int a = 10;

int main(void)
{
    a = 20;
    func();
    printf("%d", a);
    return 0;
}

void func(void)
{
    a = 30;
}

//register variable ; 블록 혹은 함수 내에 변수를 선언할 때 register 예약어를 사용한다.
//register 변수는 CPU 안에 있는 저장 공간인 register를 사용한다.
//반복문에 쓰는 변수와 같이 사용 횟수가 많은 경우 레지스터에 할당하면 실행 시간을 줄일 수 있다.

//알아야 할 점
/*
1. 전역 변수는 레지스터 변수로 선언할 수 없다.
2. 레지스터 변수는 주소를 구할 수 없다. 왜냐하면 저장 공간이 메모리에 있는 것이 아니므로 주소 연산자를 써서 구할 수 없기 때문이다.
3. 레지스터의 사용 여부는 컴파일러가 결정한다. 
 - 레지스터 변수를 선언 했다고 모두 레지스터에 변수가 생성되는 것은 아니다.
 - 컴파일러는 사용자가 레지스터 변수를 선언하더라도 레지스터와 메모리 중에 어디에 할당하는 것이 더 이득인지 판단하여 저장 공간을 선택한다.
*/
// #include <stdio.h>

// int main(void)
// {
//     register int i; //register 변수
//     auto int sum = 0; //auto 지역 변수

//     for (i = 1; i <= 10000; i++) //반복 과정에서 i를 계속 사용함
//     {
//         sum += i; //i 값을 반복하여 누적
//     }

//     printf("%d\n", sum);

//     return 0;
// }


//static variable(정적 지역 변수) ; 지역 번수를 선언할 때 static 예약어를 사용하면 정적 지역 변수가 된다. 일반 지역 변수와 같이 사용 범위가 블록 내부로 제한된다.
//반면에 저장 공간이 메모리에 존재하는 기간이 다르다.
//정적 지역 변수는 선언된 함수가 반환되더라도 그 저장 공간을 계속 유지한다. 따라서 하나의 함수가 여러 번 호출되는 경우 같은 변수를 공유하는 것이 가능하다.
//프로그램이 실행될 때 메모리에 할당되며 프로그램이 끝날 때까지 존재한다. 또한 초기화하지 않으면 0으로 자동 초기화된다.
// #include <stdio.h>
// void auto_func(void);
// void static_func(void);

// int main(void)
// {
//     int i;

//     printf("일반 지역 변수(auto)를 사용한 함수...\n");
//     for (i = 0;  i<3; i++)
//     {
//         auto_func();
//     }

//     printf("정적 지역 변수(static)를 사용한 함수...\n");
//     for (i = 0; i < 3; i++)    
//     {
//         static_func();
//     }

//     return 0;
// }

// void auto_func(void)
// {
//     auto int a = 0;

//     a++;
//     printf("%d\n", a);
// }


// void static_func(void)
// {
//     static int a;
//     a++;
//     printf("%d\n", a);
// }

//glboal variable(전역 변수)
//전역 변수는 특별한 값으로 초기화하지 않아도 0으로 자동 초기화된다.
// #include <stdio.h>

// void assign10(void);
// void assign20(void);

// int a;

// int main(void)
// {
//     printf("Before call, a : %d\n", a);

//     assign10();
//     assign20();

//     printf("After call, a : %d\n", a);

//     return 0;
// }

// void assign10(void)
// {
//     a = 100;
// }

// void assign20(void)
// {
//     int a;

//     a = 20;
// }


// #include <stdio.h>

// int main(void)
// {
//     int a = 10, b = 20;

//     printf("before commute : %d, %d\n", a, b);
//     {
//         int temp;

//         temp = a;
//         a = b;
//         b = temp;
//     }
//     printf("after commute : %d, %d\n", a, b);

//     return 0;
// }


//auto 예약어 ; 생략 가능, 이 경우 함수 안에 선언된 변수는 자동으로 지역 변수가 된다.
//local variable, auto variable은 같은 용어
//지역 변수는 자동으로 초기화되지 않는다.


// #include <stdio.h>

// void assign(void);

// int main(void)
// {
//     auto int a = 0; //지역 변수 선언과 초기화, auto는 생략 가능

//     assign();
//     printf("main 함수 a : %d\n", a);

//     return 0;
// }

// void assign(void)
// {
//     int a;

//     a = 10;
//     printf("assign 함수 a : %d\n", a);
// }