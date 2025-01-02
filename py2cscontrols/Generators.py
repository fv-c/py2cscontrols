from .Sequence import Sequence

class Transeg(Sequence):
    def generateList(self) -> list:
        transeg_list = []
        for i, segment in enumerate(self.segmentList):
            durata = segment.p2.x - segment.p1.x
            if i == 0:
                transeg_list.extend([segment.p1.y, durata, segment.segmentType, segment.p2.y])
            else:
                transeg_list.extend([durata, segment.segmentType, segment.p2.y])
        
        return transeg_list
    
    def appendoToCSFile(self, controlName: str, filepath: str):

        list = self.generateList()
        list_str = " ".join(map(str, list))

        with open(filepath, 'a') as f:
            f.write(f"{controlName} transeg {list_str}\n\n")
        
