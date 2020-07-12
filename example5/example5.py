import functools


def simple_decorator(decorator_arg):
    def additional_wrapper(func):
        @functools.wraps(func)
        def wrapper5(*args, **kwargs):
            print(f"Hey, I am decorator printing and " \
                  f"this time decorator also got argument {decorator_arg}")
            func(*args, **kwargs)
        return wrapper5
    return additional_wrapper

@simple_decorator(33)
def decorate_me(arg1, arg2):
    print(f"Hey, I am the original function with following arguments {arg1}, {arg2}")

a = decorate_me
a(2,4)
print(a.__name__)