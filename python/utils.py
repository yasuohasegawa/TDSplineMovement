import math
#https://docs.derivative.ca/Vector_Class
#https://docs.derivative.ca/Quaternion_Class

def GetRotationFromVector(target,current,direction):
    dir = (target-current)
    dir.normalize()
    
    r = GetRotationFromDirection(dir,direction)
    return r

#Z rotation will twist. It depends on what you want to create, you might need to use the LookRotation method to get a better result.
def GetRotationFromDirection(dir,direction):
    axis_align = tdu.Vector(direction)
    angle = axis_align.angle(dir)
    axis  = axis_align.cross(dir)
    #print(str(axis))
    q = tdu.Quaternion(angle, axis)
    r = q.eulerAngles(order='xyz')
    return r

#http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/
def LookRotation(target,current,direction):
    F = (target-current)
    F.normalize()

    dir = tdu.Vector(direction)
    R = dir.cross(F)
    R.normalize()

    U = F.cross(R)

    trace = R.x + U.y + F.z

    if trace > 0.0 :
        s = 0.5 / math.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (U.z - F.y) * s
        y = (F.x - R.z) * s
        z = (R.y - U.x) * s
    else:
        if R.x > U.y and R.x > F.z :
            s = 2.0 * math.sqrt(1.0 + R.x - U.y - F.z)
            w = (U.z - F.y) / s
            x = 0.25 * s
            y = (U.x + R.y) / s
            z = (F.x + R.z) / s
        elif U.y > F.z :
            s = 2.0 * math.sqrt(1.0 + U.y - R.x - F.z)
            w = (F.x - R.z) / s
            x = (U.x + R.y) / s
            y = 0.25 * s
            z = (F.y + U.z) / s
        else :
            s = 2.0 * math.sqrt(1.0 + F.z - R.x - U.y)
            w = (R.y - U.x) / s
            x = (F.x + R.z) / s
            y = (F.y + U.z) / s
            z = 0.25 * s

    q = tdu.Quaternion(x,y,z,w)
    r = q.eulerAngles(order='xyz')
    return r