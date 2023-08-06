from random import randint
import functools
#from circuitbrew.examples.parametrized import NorN
from circuitbrew.module import Module
from circuitbrew.ports import InputPorts

class decorator:
    def __init__(self, **kwargs):
        print(f'Got param {kwargs}')
        self.params = {}
        for param_name, param in kwargs.items():
            self.params[param_name] = param
    
    def __call__(self, cls):
        @functools.wraps(cls, updated=())
        class decorated(cls):
            def __init__(inner_self, *args, **kwargs):
                for param_name, param in self.params.items():
                    setattr(inner_self, param_name, param)
                super().__init__(*args, **kwargs)
        return decorated

@decorator(N=3)
class A:
    N=2
    """Hello there"""
    def foo(self):
        print("foo is here")

def Param(name):
    """Returns a new function that returns the instance variable "name" of 
       the specified instance
    """
    def lookup(self):
        v = getattr(self, name)
        return v
    return lookup

class NorN(Module):
    a = InputPorts(width=Param('N'))

    def __init__(self, *args, **kwargs):
        print('Inside NorN __init__')
        super().__init__(*args, **kwargs)

    def build(self):
        self.finalize()

class Nor3(NorN):
    def __init__(self, *args, **kwargs):
        print('Inside Nor3 __init__')
        self.N = 3
        super().__init__(*args, **kwargs)

def Parametrize(cls, **kwargs):
    """Given Param(cls, N=3, P=4), 
        it will return a new subclass of cls that has an __init__
        that sets instance vars N and P

        e.g Param(cls, N=3, P=4) is effectively returning the following:

            Class subcls_N_3_P_4(cls):
                def __init__(self, *args, **kwargs):
                    self.N = 3
                    self.P = 4
                    cls.__init__(self, *args, **kwargs)
            
    """
    params_to_str = '_'.join([f'{name}_{val}' for name, val in kwargs.items()])

    def init_fn(self, *a, **kw):
        for name, val in kwargs.items():
            setattr(self, name, val)
        cls.__init__(self, *a, **kw)

    parametrized_class = type(f'{cls.__name__}_{params_to_str}', (cls,), 
                              { '__init__': init_fn })

    return parametrized_class

def main():
    n = Parametrize(NorN, N=3)()

if __name__=='__main__':
    a = A()