class A:
    def __init__(self,x):
        self.x=x
    def getX(self):
        print("Ax: "+str(self.x))

class B(A):
    def __init__(self,y,x):
        self.y=y
        super().__init__(x)
    def getY(self):
        print("By: "+str(self.y))
        
obj=B(10,20)
obj.getX()
obj.getY()