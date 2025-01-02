import os

from .Generators import Transeg

class Control:
    def __init__(self, controlName: str , transeg: Transeg):
        self.controlName = controlName
        self.transeg = transeg
    
    def appendoToCSDFile(self, filepath: str):

        list = self.transeg.generateList()
        list_str = " ".join(map(str, list))

        with open(filepath, 'a') as f:
            f.write(f"{self.controlName} transeg {list_str}\n\n")
        
        print(f"{self.controlName} written on {os.path.abspath(filepath)}")