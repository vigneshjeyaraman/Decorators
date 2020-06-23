
def simple_decorator(func):
    def wrapper():
        print("Hey I am decorating you buddy")
        func()
        print("I decorated you.")
    return wrapper

@simple_decorator
def decorate_me():
    print("Someone is going to get call before me :P")


decorate_me()