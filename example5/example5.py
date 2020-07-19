import functools


class Decorator:
    '''We will be using this class for decorating functions'''
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def wrapper(a, b):
            print("__call__ called before decorating function3")
            func(a,b)
            print(f"class arguments are {self.arg1}, {self.arg2}")
        return wrapper
    
@Decorator(1,2)
def function3(a,b):
    print(f"I am decorated and argument passed are {a}, {b}")

function3(2,3)
