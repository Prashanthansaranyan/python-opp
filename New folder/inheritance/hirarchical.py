class A:
    def __init__(self):
        self.x = 10

    def getX(self):
        print("Ax: " + str(self.x))


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20

    def getY(self):
        print("By: " + str(self.y))


class C(A):
    def __init__(self):
        super().__init__()
        self.z = 30

    def getZ(self):
        print("Cz: " + str(self.z))


obj = C()
obj.getX()
obj.getZ()

obj = B()
obj.getY()
obj.getX()