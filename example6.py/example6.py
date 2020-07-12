import functools


def simple_decorator(func):
    @functools.wraps(func)
    def wrapper6(*args, **kwargs):
        wrapper6.count_calls += 1
        print(f"Hey, I am decorator printing")
        print(f"I am called {wrapper6.count_calls} times")
        func(*args, **kwargs)
    wrapper6.count_calls = 0
    return wrapper6

@simple_decorator
def decorate_me():
    print(f"Hey, I am the original function")

for i in range(4):
    decorate_me()