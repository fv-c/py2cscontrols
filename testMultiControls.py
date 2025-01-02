from py2cscontrols import Point, Segment, Transeg, Control

pA1 = Point(0, 0)
pA2 = Point(1, 1)
segA = Segment(pA1, pA2, 0)

pB1 = Point(0, 0)
pB2 = Point(0.5, 1)
pB3 = Point(1, 0)
segB1 = Segment(pB1, pB2, 2)
segB2 = Segment(pB2, pB3, -2)


transegA = Transeg([segA])
transegB = Transeg([segB1, segB2])

transegA.saveSequencePlot("testMultiControlsA.pdf")
transegB.saveSequencePlot("testMultiControlsB.pdf")

gktestMultiControlsA = Control("gktestMultiControlsA", transegA)
gktestMultiControlsB = Control("gktestMultiControlsB", transegB)

gktestMultiControlsA.appendoToCSDFile("testMultiControls.csd")
gktestMultiControlsB.appendoToCSDFile("testMultiControls.csd")