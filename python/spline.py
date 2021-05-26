import math
#https://docs.derivative.ca/Vector_Class
#https://docs.derivative.ca/Quaternion_Class
#https://docs.derivative.ca/Matrix_Class

class Spline:
    maxPoints = 0
    numberOfSegments = 0
    TOTAL = 0

    controlPoints = []
    positions = []

    def __init__(self,max,segments):
        self.maxPoints = max
        self.numberOfSegments = segments
        self.TOTAL = self.maxPoints * self.numberOfSegments

    def SetupPoints(self, points):
        self.controlPoints = points
        for i in range(self.TOTAL):
            self.positions.append(tdu.Vector([0,0,0]))

    def CreateAndUpdateHermitecurve(self):
        if self.numberOfSegments < 2:
            self.numberOfSegments = 2

        p0 = tdu.Vector()
        p1 = tdu.Vector()
        m0 = tdu.Vector()
        m1 = tdu.Vector()

        last = len(self.controlPoints) - 1
        ind = 0
        for j in range(last):
            
            if (self.controlPoints[j] is None) or (self.controlPoints[j+1] is None) or (j > 0 and self.controlPoints[j-1] is None) or (j < len(self.controlPoints)-2 and self.controlPoints[j+1] is None):
                return
            
            p0 = self.controlPoints[j]
            p1 = self.controlPoints[j+1]
            if j > 0:
                m0 = 0.5 * (self.controlPoints[j + 1] - self.controlPoints[j - 1])
            else:
                m0 =  self.controlPoints[j + 1] -  self.controlPoints[j]

            if j < len(self.controlPoints) - 2:
                m1 = 0.5 * (self.controlPoints[j + 2] - self.controlPoints[j])
            else:
                m1 = self.controlPoints[j + 1] - self.controlPoints[j]
            
            position = tdu.Vector()
            t = 0.0
            pointStep = 1.0 / self.numberOfSegments

            if j ==  len(self.controlPoints) - 2:
                pointStep = 1.0 / (self.numberOfSegments - 1.0)

            for i in range(self.numberOfSegments):
                t = i * pointStep
                position = (2.0 * t * t * t - 3.0 * t * t + 1.0) * p0 + (t * t * t - 2.0 * t * t + t) * m0 + (-2.0 * t * t * t + 3.0 * t * t) * p1 + (t * t * t - t * t) * m1

                if ind < len(self.positions):

                    self.positions[ind] = position

                    ind += 1