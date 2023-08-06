import inspect
class A:
    def __init__(self):
        print(self.__class__.__name__)


class B(A):
    def foo(self):
        print('hello B')

if __name__=='__main__':
    b = B()
    for cls in inspect.getmro(B):
        print(cls.__name__)
    