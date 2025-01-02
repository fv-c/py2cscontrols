import numpy as np
import matplotlib.pyplot as mpt

from .Point import Point

class Segment:
    def __init__(self, p1: Point, p2: Point, segmentType: float = 0):
        self.p1 = p1
        self.p2 = p2
        self.segmentType = segmentType
    
    def calculateCurve(self, steps=100) -> tuple:
        x_values = np.linspace(self.p1.x, self.p2.x, steps)
        y_values = []

        A = self.p1.y
        B = self.p2.y
        n = steps
        itype = self.segmentType

        for i in range(steps):
            if itype == 0:
                y = A + (B - A) * (i / (steps - 1))
            else:
                numerator = 1 - np.exp(i * itype / (n - 1))
                denominator = 1 - np.exp(itype)
                y = A + (B - A) * (numerator / denominator)
            
            y_values.append(y)
        
        return x_values.tolist(), y_values
    
    def plotSegment(self):
        x, y = self.calculateCurve()
        mpt.plot(x, y)
        mpt.scatter([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], color='red')
        mpt.xlabel('X')
        mpt.ylabel('Y')
        mpt.title('Segment Visualization')
        mpt.grid(True)
        mpt.show()