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


class C(A):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z

    def getZ(self):
        print("Cz: " + str(self.z))


obj = C(10,50)
obj.getX()
obj.getZ()

obj = B(10,20)
obj.getX()
obj.getY()