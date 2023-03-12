//calloc 함수 : 할당한 저장 공간을 0으로 초기화, 메모리를 동적으로 할당하여 0으로 초기화된 메모리 공간을 얻고자 할 때 사용한다.
//realloc 함수 : 크기를 조절

//the prototpyes of calloc, realloc function
//storage class(기억 부류) ; 프로그램은 실행될 때 일정한 메모리 영역을 사용한다. 이 영역은 다시 몇 개의 영역으로 나뉘어 관리된다. 이를 기억 부류라고 한다.
//기억 부류는, 프로그램이 올라가는 코드 영역과, 데이터가 저장되는 데이터 영역으로 나눈다.
// 데이터 영역은 지역 변수들이 할당되는 스택(stack) 영역이 있고, 동적 할당되는 저장 공간은 힙(heap) 영역을 사용한다.
// 그 외에 global variable이나 static variable을 위한 데이터 영역이 있다.

// healp에 할당된 저장 공간은 지역 변수와 마찬가지로 garbage value 가 있다. 그러나 지역 변수와 달리 프로그램이 종료될 때까지 메모리에 존재한다.
// 따라서 주소만 알면 특정 함수에 구애 받지 않고 어디서나 사용할 수 있다.
// 지역 변수와 달리 동적 할당된 저장 공간은 함수가 반환되어도 메모리가 회수되지 않는다.

// 메모리에 저장 공간이 넉넉하게 남아 있어도 메모리 할당 함수들이 널 포인터를 반환할 수 있다.
// 힙 영역은 메모리의 사용과 반환이 불규칙적이기 때문에 사용 가능한 영역이 조각나서 흩어져 있을 수 있다.
// 이때 연속된 큰 저장 공간을 요구하면 동적 할당 함수는 원하는 저장 공간을 찾지 못하고 널 포인터를 반환할 수 있다.

// void *calloc(unsigned int, unsigned int);

// void *realloc(void *, unsigned int);

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pi;
    int size = 5;
    int count = 0;

    int num;
    int i;

    pi = (int *)calloc(size, sizeof(int)); // 먼저 5개의 저장 공간을 할당
    while (1)
    {
        printf("양수만 입력 => ");
        scanf("%d", &num);
        if (num <= 0) break; // 0 또는 음수이면 종료
        if (count == size) // 저장 공간을 모두 사용하면
        {
            size += 5; // 크기를 늘려서 재할당, resizing
            pi = (int *)realloc(pi, size * sizeof(int)); // resizing을 할 때 크기를 키우면, 추가된 공간에는 garbage value가 존재한다. 크기를 줄이면 입력된 데이터가 잘려나간다.
            //재할당 과정에서 메모리의 위치가 바뀔 수 있으므로 다시 포인터에 저장해 사용하는 것이 좋다.
        }
        pi[count++] = num;
    }
    for (i = 0; i < count; i++)
    {
        printf("%5d", pi[i]);
    }
    free(pi);

    return 0;
}