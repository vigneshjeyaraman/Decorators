import functools


def count_calls(func):
    '''Function to keep track how many times function is called'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Function is called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

def cache(func):
    '''Function to store already calculated value in fibonacci'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args, **kwargs)
        return wrapper.cache[args]
    
    wrapper.cache = dict()
    return wrapper

@cache    
@count_calls
def fib(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)

fib(12)