from A,B import A,B
class C(A, B):
    def __init__(self):
        A.__init__(self)  
        B.__init__(self)
        self.z = 30

    def getZ(self):
        print("Cz: " + str(self.z))