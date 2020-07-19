class Practice:
    """Class to show the use of call method"""
    def __init__(self, *args, **kwargs):
        print("Hey, I am __init__")

    def __call__(self, *args, **kwargs):
        print("Hey, I am __call__")

obj2 = Practice()
obj2()
print(callable(obj2))