from multilevelB import B 
class C(B):
    def __init__(self):
        super().__init__()
        self.z = 30

    def getZ(self):
        print("Cz: " + str(self.z))