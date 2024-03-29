/*
complie 과정
1. 소스파일을 전처리한다.
2. 전처리된 소스파일을 컴파일하면 개체 파일이 된다.
3. 개체 파일을 링크하면 실행파일이 된다.

전처리는 전처리기(preprocessor)가 소스 코드를 컴파일하기 좋게 다듬는 과정이며 
소스 코드에서 #으로 시작하는 지시자를 처리한다.

전처리 과정은 소스 파일에 다른 파일의 내용을 포함시키거나 일부 문장을 다른 문장으로 바꾸는 등 
소스 파일을 편집하는 일을 주로 수행하므로
전처리된 후의 파일도 소스 파일과 형태가 같은 텍스트 파일이다.
*/

/*
#include : 지정한 파일의 내용을 읽어와 지시자가 있는 위치에 붙여놓는다. 
           붙여넣을 파일명을 꺽쇠괄호(<>)나 큰따옴표("")로 묶는다.

           꺽쇠괄호(<>)를 사용하면 복사할 파일을 컴파일러가 설정한 include 디렉터리에서 찾는다.
           큰따옴표를 사용하면 소스 파일이 저장된 디렉터리에서 먼저 찾는다.
           만약 해당 파일이 없으면 컴파일러가 설정한 include 디렉터리에서 다시 한번 찾는다.

           C 컴파일러는 표준 라이브러리 함수가 포함된 헤더 파일을 include 디렉터리에서 제공한다.
           #include 다음에 꺽쇠괄호가 보이면 컴파일러의 include 디렉터리에서 헤더 파일을 참조한다.
           즉, 꺽쇠괄호는 컴파일러가 제공하는 파일이고, 큰따옴표는 사용자가 만든 헤더 파일을 나타낸다.

           다른 데릭터리에 있는 파일을 포함할 때는, 경로를 포함한 파일명을 사용한다.
           ex. #incldue "c:\user\eon\Onedrive\Practice\myhdr.h" // 프로젝트 디렉터리가 아닌 곳에서 찾는다.
           이때 백슬래시는 한 번만 사용한다.
           전처리 지시자는 컴파일러가 사용하는 것이 아니므로 백슬래시를 제어 문자로 사용하지 않는다.

           #include는 파일의 내용을 단순히 복사하여 붙여넣는 기능을 한다.
           따라서 텍스트 형태의 파일이면 모두 사용할 수 있다.
           심지어 소스 파일을 포함할 수도 있다.
           main 함수의 중간에 들어가는 코드를 따로 뗴어 헤더 파일로 만든 후에 인클루드하는 것도 가능하다.
           int main(void)
           {
            #incldue "myhdr.c"
                return 0;
           }
*/

/*
하나의 프로그램은 독립적으로 컴파일 가능한 파일 단위인 모듈(module)로 나누어 분할 컴파일한다.
따라서 각 모듈이 같이 사용하는 구조체나 함수 또는 전역 변수를 하나의 헤더 파일로 만들면
필요한 모듈에서 쉽게 포함하여 쓸 수 있다.
이 경우 헤더 파일의 내용이 수정되더라도 컴파일만 다시 하면 수정된 내용이 모든 파일에 동시에 적용되므로
빠르고 정확하게 수정할 수 있다.
*/

/*
#define 
매크로명을 정의하는 전처리 지시자이다.
매크로명은 다른 변수명과 쉽게 구분할 수 있도록 관례상 대문자로 쓰며 
치환될 부분은 매크로명과 하나 이상의 빈칸을 둔다.

#define 매크로명 치환될_부분
*/

// #include <stdio.h>
// #define PI 3.14159
// #define LIMIT 100.0
// #define MSG "passed"
// #define ERR_PRN printf("Do not allowed.")

// int main(void)
// {
//     double radius, area;

//     printf("input radius(under 10) : ");
//     scanf("%lf", &radius);
//     area = PI * radius *radius;
//     if (area > LIMIT) ERR_PRN;
//     else printf("area of circle : %.2lf (%s)\n", area, MSG);

//     return 0;
// }

/*
프로그램에서 사용한 모든 매크로명은 전처리 과정에서 치환될 부분으로 바뀐다.
상수 대신에 쓰이는 매크로명은 '매크로 상수'라고 부른다.

매크로명을 정의할 때 치환될 부분이 길어서 여러 줄에 써야 한다면 백슬래시(\)로 연결한다.
#deifne INTRO "Perfect C Language \
& Basic Data Structure"
*/


/*
매크로 함수를 만들 때 매크로 연산자를 사용하면 인수를 특별한 방법으로 치환할 수 있다.
#은 매크로 함수의 인수를 문자열로 치환하고
##은 두 인수를 붙여서 치환한다. 

## 연산자는 2개의 토큰(token)을 붙여서 하나로 만드는 연산자이다.
토큰은 프로그램에서 독립된 의미를 갖는 하나의 단위로,
      예제에서는 각각 다른 2개의 토큰 a와 1을 하나로 붙여서 면수명 a1으로 사용하도록 치환한다.
*/

#include <stdio.h>
#define PRINT_EXPR(x) printf(#x " = %d\n", x)
#define NAME_CAT(x,y) (x ## y)

int main(void)
{
    int a1, a2;

    NAME_CAT(a, 1) = 10; //(a1) = 10
    NAME_CAT(a, 2) = 20; //(a2) = 20
    PRINT_EXPR(a1 + a2); // printf("a1+a2" " = %d\n", a1+a2);

    return 0;
}