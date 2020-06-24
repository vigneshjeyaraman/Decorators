
def simple_decorator(func):
    def wrapper1():
        print("Hey, I am decorating you buddy")
        func()
        print("I decorated you.")
    return wrapper1

@simple_decorator
def decorate_me():
    print("Someone is going to get call before me :P")


decorate_me()