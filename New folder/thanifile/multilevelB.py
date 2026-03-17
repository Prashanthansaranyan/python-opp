from maltilevelA import A 
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20

    def getY(self):
        print("By: " + str(self.y))
