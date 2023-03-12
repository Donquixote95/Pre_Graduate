#include <stdio.h>
#include <stdlib.h>
//stdlib.h에 선언된 malloc 함수와 free 함수의 prototype
/*
void *malloc(unsigned int size);
void free(void *p);
*/

int main(void)
{
    int *pi;
    double *pd;

    pi = (int *)malloc(sizeof(int)); // 메모리 동적 할당 후 포인터 연결
    //sizeof(int) ; int형 변수의 크기
    //malloc(sizeof(int)) ; 저장공간을 할당하고 (void*)형 반환
    //malloc 함수는 void *형을 반환하기 때문에 용도에 맞는 포인터형으로 형 변환하여 사용한다.
    //(int *) 반환되는 주소를 int형 변수의 주소로 형 변환
    
    if (pi == NULL)
    {
        printf("# 메모리가 부족합니다.\n");
        exit(1);    // 프로그램 종료
        //exit 함수는 main 함수뿐만 아니라 어떤 함수에서든 프로그램을 바로 종료할 수 있으며, 예외 상황이 발생하여 프로그램을 바로 종료해야 하는 경우 인수를 1로 주고 호출한다.
    }
    pd = (double *)malloc(sizeof(double));

    *pi = 10;
    *pd = 3.4;

    printf("정수형으로 사용 : %d\n", *pi); //동적 할당 영역에 저장된 값 출력
    printf("실수형으로 사용 : %.1lf\n", *pd);

    free(pi);
    free(pd);

    return 0;
}

/*
주의 1. malloc 함수의 반환값이 널 포인터인지 반드시 확인하고 사용해야 한다.
메모리 할당 함수는 원하는 크기의 공간을 할당하지 못하면 0번지인 널 포인터(null pointer)를 반환한다. null pointer는 보통 NULL로 표기하는데
Procedure process(전처리 단계)에서 0으로 바뀌므로 정수 0과 같다고 생각해도 무방하다.
널 포인터는 포인터의 특별한 상태를 나타내기 위해 사용하므로 간접 참조 연산을 할 수 없다.
따라서 malloc 함수가 널 포인터를 반환한 경우 그 값을 참조하면 실행 중에 에러 메시지를 표시하고 비정상 종료된다.
*/

/*
주의 2. allocation 이후에는 free 함수를 이용해서 저장 공간을 return 해야 한다.
하지 않으면, memory leak(메모리 누수)를 일으켜서 프로그램이 의도치 않게 종료될 수 있다.
main 함수가 끝날 때, 프로그램에서 동적으로 할당한 저장 공간은 운영체제에 의해서 자동으로 회수된다.
따라서 main 함수가 끝날 때는 굳이 반환할 필요가 없지만 그 외 다른 함수에서 사용하던 저장 공간은 불필요한 경우 반환하여 새로운 동적 할당에 재활용해야 한다.
*/