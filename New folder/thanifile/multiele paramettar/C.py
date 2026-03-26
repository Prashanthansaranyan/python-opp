from A import A
from B import B

class C(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x)
        B.__init__(self, y)
        self.z = z

    def getZ(self):
        print("Cz:", self.z)