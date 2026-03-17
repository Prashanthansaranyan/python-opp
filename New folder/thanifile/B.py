from A import A
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def getY(self):
        print("By: " + str(self.y))