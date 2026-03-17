from A import A
class C(A):
    def __init__(self):
        super().__init__()
        self.z = 30

    def getZ(self):
        print("Cz: " + str(self.z))