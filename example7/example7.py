from dataclasses import dataclass


@dataclass
class Test1:
    pass

obj1 = Test1()
print(obj1)


@dataclass
class Test2:
    arg1: int
    arg2: int

obj2 = Test2(2,3)
print(obj2, obj2.arg1)