import random

from py2cscontrols import Point, Segment, Transeg, Control

#----

n = 20
x_points = [0] + [random.randint(0, 10000) for _ in range(n-1)]
y_points = [0] + [random.random() for _ in range(n-1)]
segmentTypeList = [random.uniform(-10, 10) for _ in range(n-1)]

pp = []
segs = []

pairs = sorted(zip(x_points, y_points), key=lambda pair: pair[0])

for pair in pairs:
    pp.append(Point(pair[0],pair[1]))

for i in range(len(pp) - 1):
    segs.append(Segment(
        pp[i], 
        pp[i + 1], 
        segmentTypeList[i]
        )
    )

transeg = Transeg(segs)

transeg.saveSequencePlot("testRandom.pdf")

gktest = Control("gktestRandom", transeg)

gktest.appendoToCSDFile("testRandom.csd")
