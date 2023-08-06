from random import randint
import functools
#from circuitbrew.examples.parametrized import NorN
class Descriptor:
    def __get__(self, instance, owner):
        print("Getting value from descriptor")
        return instance._value

    def __set__(self, instance, value):
        print("Setting value in descriptor")
        instance._value = value

    def __delete__(self, instance):
        print("Deleting value in descriptor")
        del instance._value

    def __set_name__(self,cls,name):
        print(f"Got name {name}")

class ClassDecorator:
    def __init__(self, cls):
        print("Initializing ClassDecorator")
        self._cls = cls

    def __call__(self, *args, **kwargs):
        print("Class decorator called")
        instance = self._cls(*args, **kwargs)
        print("Instance of the decorated class created")
        return instance

@ClassDecorator
class MyClass:
    value = Descriptor()

    def __init__(self, value):
        print("Initializing MyClass")
        self._value = value

# Execution flow
print("Creating an instance of MyClass")
obj = MyClass(42)
print("Accessing obj.value")
print(obj.value)
print("Updating obj.value")
obj.value = 24
print("Deleting obj.value")
del obj.value