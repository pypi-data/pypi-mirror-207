from .wchb_01 import Wchb
from circuitbrew.module import Module

class Main(Module):
    def build(self):
        self.wchb = Wchb()
        self.finalize()