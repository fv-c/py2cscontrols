from py2cscontrols import Point, Segment, Transeg, Control

#----

p1 = Point(0, 0)
p2 = Point(1, 1)

seg1 = Segment(p1, p2, 0)

transeg = Transeg([seg1])

transeg.saveSequencePlot("test0.pdf")

gktest = Control("gktest0", transeg)

gktest.appendoToCSDFile("test0.csd")
