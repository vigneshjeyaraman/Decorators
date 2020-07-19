class Decorator:
    '''We will be using this class for decorating functions'''
    def __init__(self, func):
        self._fun = func
    
    def __call__(self, a, b):
        print("__call__ called before decorating function1")
        self._fun(a,b)
    
    def class_method(self):
        print("I am called by a decorated function")

@Decorator
def function1(a, b):
    print(f"I am decorated and argument passed are {a}, {b}")

function1(2,4)
function1.class_method()