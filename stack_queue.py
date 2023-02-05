# IS-A 관계 ;  ~는 ~이다, 상속에 활용
# HAS-A 관계 ; ~가 ~를 갖는다, 구성(composition)에 활용

# 구성(composition) ; 다른 클래스를 갖고, 필요할 때 활용


# stack ; LIFO 구조
# 스택 안에 넣는 것 push, 꺼내는 것 pop

# queue ; FIFO 구조
# 큐 안에 넣는 것 enqueue, 꺼내는 것 dequeue

# 파이썬의 리스트는 스택과 큐의 기능을 모두 갖고 있다.
# 그러나 Stack이라는 새로운 클래스를 만들어서 사용하는 방법이 있다.
# Stack has-a List(스택 클래스가 리스트를 갖게 구성)
# 리스트를 스택으로만 사용하게 제한하는 것

class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())


# 큐 구현하기
class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self, item):
        self.list.append(item)
    def dequeue(self):
        return self.list.pop(0)
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())