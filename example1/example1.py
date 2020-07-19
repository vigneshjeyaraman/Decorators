class Practice:
    """Class to show the use of call method"""
    def __init__(self, *args, **kwargs):
        print("Hey, I am __init__")

obj1 = Practice()
print(callable(obj1))