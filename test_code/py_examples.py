from types import MethodType

class obj():
    def __init__(self):
        self.x = 1

def my_method(self):
    print(self.x)

def func(self, x):
    return self.x + x

if __name__ == "__main__":
    o = obj()
    setattr(o, "foo", my_method.__get__(o, o.__class__))
    o.foo()
    print(o.__class__)
    o.method = MethodType(func, o)
    result = o.method(5)
    print(result)