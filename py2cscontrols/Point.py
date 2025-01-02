class Point:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def xyC(self) -> list:
        return [self.x, self.y]
    
    def xyzC(self) -> list:
        return [self.x, self.y, self.z]