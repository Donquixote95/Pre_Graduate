#include <stdio.h>

int main(void){

    //조건 연산자, 삼항 연산자이다. ?와 :를 사용한다.
    //첫 번째 피연산자가 참이면 두 번쨰 피연산자가가 결과값이 되고
    //첫 번째 피연산자가 거짓이면 세 번째 피연산자가 결과값이 된다.

    int a = 10, b= 20, res;

    res = (a>b) ? a : b;
    // (a>b)?(res = a) : (res = b); 와 같이 해도 같은 결과가 나온다.
    printf("큰 값 : %d\n",res);

    // comma operation(,) ; 한 번에 여러 개의 수식을 차례로 나열해야 할 때 사용한다.
    // 왼쪽부터 오른쪽으로 차례로 연산을 수행하며 가장 오른쪽의 피연산자가 최종 결과값이 된다.
    // 콤마 연산자는 대입 연산자보다 우선순위가 낮은 유일한 연산자이다. 따라서 대입 연산자와 함꼐 사용할 떄는 괄호가 필요하다.
    // int a= 10, b = 20;
    // int res;

    // res = (++a, ++b);

    // printf("a:%d, b:%d\n", a, b);
    // printf("res:%d\n", res);

    // int a = 10, b = 20;
    // int res = 2;

    // a+=20;
    // res *= b + 10;

    // printf(" a= %d, b = %d\n", a, b);
    // printf("res = %d\n", res);

    // sizeof 연산자는 피연산자의 크기를 바이트 단위로 알려준다.
    // int a = 10;
    // double b = 3.4;

    // printf("int형 변수의 크기 : %d\n", sizeof(a));
    // printf("double형 변수의 크기 : %d\n", sizeof(b));
    // printf("정수형 상수의 크기 : %d\n", sizeof(10));
    // printf("수식의 결과값의 크기 : %d\n", sizeof(1.5 + 3.4));
    // printf("char 자료형의 크기 : %d\n", sizeof(char));

    // int a = 20, b = 3;
    // double res;

    // res = ((double)a) / ((double)b);
    // printf("a = %d, b = %d\n", a, b);
    // printf("a / b의 결과 : %.1lf\n", res);

    // a = (int)res;
    // printf("(int) %.1lf의 결과 : %d\n", res, a);

    // int a = 10, b = 20, res;
 
    // a+b;
    // printf("%d + %d = %d\n", a, b, a+b);

    // res = a + b;
    // printf("%d + %d = %d\n", a, b, res);

    // int a = 30;
    // int res;

    // res = (a > 10) && (a<20);
    // printf("(a>10) && (a<20) : %d\n", res);
    // res = (a<10) || (a>20);
    // printf("(a<10) || (a>20) : %d\n", res);
    // res = !(a>=30);
    // printf("!(a>30) : %d\n", res);

    // int a = 10, b = 20, c = 10;
    // int res;

    // res = (a > b);
    // printf("a>b : %d\n", res);
    // res = (a >= b);
    // printf("a>=b : %d\n", res);
    // res = (a < b);
    // printf("a<b : %d\n", res);
    // res = (a == b);
    // printf("a==b : %d\n", res);
    // res = (a != b);
    // printf("a!=b : %d\n", res);

    // int a, b;
    // int sum, sub, mul, inv;

    // a = 10;
    // b = 20;
    // sum = a+b;
    // sub = a-b;
    // mul = a*b;
    // inv = -a;

    // printf("a의 값 : %d, b의 값 : %d\n", a, b);
    // printf("덧셈 : %d\n", sum);
    // printf("뺄셈 : %d\n", sub);
    // printf("곱셈 : %d\n", mul);
    // printf("a의 음수 연산 : %d\n", inv);

    // double apple;
    // int banana;
    // int orange;

    // apple = 5.0 / 2.0;
    // banana = 5/2;
    // orange = 5%2;

    // printf("apple : %.1lf\n", apple);
    // printf("banana : %d\n", banana);
    // printf("orange : %d\n", orange);

    // int x = 10, y = 10;

    // ++x;
    // --y;

    // printf("x : %d\n", x);
    // printf("y : %d\n", y);

    // int p = 5, q = 5;
    // int pre, post;

    // pre = (++p) * 3;
    // post = (q++) * 3;

    // printf("초깃값 p = %d, q = %d\n", p, q);
    // printf("전위형: (++p) *3 = %d, 후위형: (q++) * 3 = %d\n", pre, post);

    return 0;
}

// &&논리곱(AND)
// ||논리합(OR)
// !논리부정(NOT)

//short circuit rule(숏 서킷 룰) ; 좌항만으로 &&와 || 연산 결과를 판별하는 기능


//자동 형 변환(암시적인 형 변환) ; 컴파일러는 컴파일 과정에서 피연산자의 형태가 다르면 형태를 일치시킨다.
// 규칙 1. 크기가 작은 값이 크기가 큰 값으로 바뀐다.
// 규칙 2. 대입 연산은 메모리에 값을 저장하므로 좌항의 변수형에 맞게 저장된다.