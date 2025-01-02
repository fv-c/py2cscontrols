import os

from .Segment import Segment
import matplotlib.pyplot as mpt

class Sequence:
    def __init__(self, segmentList: list, seqName: str = 'Sequence'):
        if not all(isinstance(segment, Segment) for segment in segmentList):
            raise TypeError("Expected a list of Segment objects.")
        
        self.segmentList = segmentList
        self.seqName = seqName

    def plotSequence(self):
        for segment in self.segmentList:
            x, y = segment.calculateCurve()
            mpt.plot(x, y)
        
        for segment in self.segmentList:
            mpt.scatter([segment.p1.x, segment.p2.x], [segment.p1.y, segment.p2.y], color='red')
        
        mpt.xlabel('milliseconds')
        mpt.title(self.seqName)
        mpt.grid(True)

        ax = mpt.gca()
        ax.set_aspect('auto')

        mpt.show()
    
    def saveSequencePlot(self, filename='plot.pdf'):
        fig, ax = mpt.subplots()
        
        for segment in self.segmentList:
            x, y = segment.calculateCurve()
            ax.plot(x, y)
        
        for segment in self.segmentList:
            ax.scatter([segment.p1.x, segment.p2.x], [segment.p1.y, segment.p2.y], color='red')
        
        ax.set_xlabel('milliseconds')
        ax.set_title(self.seqName)
        ax.grid(True)
        ax.set_aspect('auto')

        fig.savefig(filename)
        mpt.close(fig)

        print(f"Sequence plot saved as {os.path.abspath(filename)}")