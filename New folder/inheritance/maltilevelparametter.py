class A:
    def __init__(self, x):
        self.x = x

    def getX(self):
        print("Ax: " + str(self.x))


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def getY(self):
        print("By: " + str(self.y))


class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def getZ(self):
        print("Cz: " + str(self.z))


obj = C(10, 20, 50)
obj.getX()
obj.getY()
obj.getZ()