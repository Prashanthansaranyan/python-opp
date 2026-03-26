from A import A
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20
        self.x = 30

    def getY(self):
        print("By: " + str(self.y))
    def getX(self):
        print("Ax: " + str(self.x))