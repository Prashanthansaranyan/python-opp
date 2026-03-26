from B import B
class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def getZ(self):
        print("Cz: " + str(self.z))