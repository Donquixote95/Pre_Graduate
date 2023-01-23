x = 1
print(x + 2 == x.__add__(2))
print()

class complex_number:
    def __init__(self, v, i):
        self.real_part = v
        self.imaginary_part = i
    def __add__(self, other):
        return complex_number(self.real_part + other.real_part,
                              self.imaginary_part + other.imaginary_part)
    def __eq__(self, other):
        return self.real_part == other.real_part and \
                self.imaginary_part == other.imaginary_part

print(complex_number(5, 7) == complex_number(1, 2) + complex_number(4, 5))
print()

print(isinstance(1, int))
print()

class foo:
    def __init__(self, v, type_):
        self.value = v
        self.type_ = type_
    def __eq__(self, other):
        if isinstance(other, foo):
            return self.value == other.value
        return False
f1, f2 = foo(1, 'type_1'), foo(1, 'type_2')
print(f1 == f2)

class Mammal:
    def __init__(self) -> None:
        self.lay_egg = False
        self.breast_feed = True
    
    def sound(self) -> None:
        return None
    
class Wolf(Mammal):
    def __init__(self) -> None:
        super().__init__()
        self.is_furry = True
        self.is__carnivore = True

    def sound(self) -> str:
        return "아우우우"
    
class Dog(Wolf):
    def __init__(self) -> None:
        super().__init__()
        self.ability = "can pet it"

    def sound(self) -> str:
        return "멍멍"
    
class Horse(Mammal):
    def __init__(self) -> None:
        self.is_furry = True
        self.is_carnivore = False
        self.ability = "can ride on it"

    def sound(self) -> None:
        return "히히힝"

my_horse = Horse()
print(my_horse)
print(my_horse.is_carnivore)

my_dog = Dog()
print(my_dog.breast_feed)

print(isinstance(Dog(), Mammal))

print(Dog().sound() != Wolf().sound())