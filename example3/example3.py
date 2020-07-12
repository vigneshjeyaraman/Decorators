def simple_decorator(func):
    def wrapper3():
        print("Hey, I am decorator printing")
        func()
    return wrapper3

@simple_decorator
def decorate_me():
    print("Hey, I am the original function")

a = decorate_me
a()
print(a.__name__)
