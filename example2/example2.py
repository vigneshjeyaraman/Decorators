def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hey I am decorating you buddy")
        func(*args, *kwargs)
        print("I decorated you.")
    return wrapper

@simple_decorator
def decorate_me(arg1, arg2):
    print(f"Hey I have received two argruments {arg1 !r} and {arg2 !r}")


decorate_me("one", "two")