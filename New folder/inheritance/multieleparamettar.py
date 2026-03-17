class A:
    def __init__(self,x):
        self.x = x

    def getX(self):
        print("Ax: " + str(self.x))


class B:
    def __init__(self,y):
        self.y = y

    def getY(self):
        print("By: " + str(self.y))


class C(A, B):
    def __init__(selfx,y,z):
        A.__init__(self,x)  
        B.__init__(self,y)
        self.z = z

    def getZ(self):
        print("Cz: " + str(self.z))


obj = C(10,20,30)
obj.getX()
obj.getY()
obj.getZ()