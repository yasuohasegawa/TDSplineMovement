import math
#https://docs.derivative.ca/Vector_Class
#https://docs.derivative.ca/Quaternion_Class
#https://docs.derivative.ca/ObjectCOMP_Class

proj = op('/project1')

v = tdu.Vector()
points =[]
sopOrCam = 'boxtrans'
cam = op(sopOrCam).par
camV = tdu.Vector()
next = 1

def Start():
    global sp
    m = proj.ops('transform*')
    for a in m:
        if a.name != "transform_render" and a.name != "boxtrans":
            points.append(tdu.Vector([a.par.tx,a.par.ty,a.par.tz]))
    
    cam.tx = points[0].x
    cam.ty = points[0].y
    cam.tz = points[0].z
    
    points.append(points[0])

    sp = mod.spline.Spline(len(points)-1,80)
    sp.SetupPoints(points)
    sp.CreateAndUpdateHermitecurve()

def Update():
    if len(sp.positions) == 0:
        return

    camV.x = cam.tx
    camV.y = cam.ty
    camV.z = cam.tz

    global next

    next += 1
    if next % sp.TOTAL == 0:
        next = 0

    v = camV.lerp(sp.positions[next],0.05)
    cam.tx = v.x
    cam.ty = v.y
    cam.tz = v.z
    
    r = mod.utils.LookRotation(sp.positions[next], camV, [0.0, 1.0, 0.0])
    cam.rx = r[0]
    cam.ry = r[1]
    cam.rz = r[2]

    '''
    r = mod.utils.GetRotationFromVector(sp.positions[next], camV, [0.0, 0.0, 1.0])
    cam.rx = r[0]
    cam.ry = r[1]
    cam.rz = r[2]
    '''

Start()
