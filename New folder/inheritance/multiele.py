class A:
    def __init__(self):
        self.x = 10

    def getX(self):
        print("Ax: " + str(self.x))


class B:
    def __init__(self):
        self.y = 20

    def getY(self):
        print("By: " + str(self.y))


class C(A, B):
    def __init__(self):
        A.__init__(self)  
        B.__init__(self)
        self.z = 30

    def getZ(self):
        print("Cz: " + str(self.z))


obj = C()
obj.getX()
obj.getY()
obj.getZ()