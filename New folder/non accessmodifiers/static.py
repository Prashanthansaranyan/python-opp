class A:
    @abstractmethod
    def getx(self):
        pass
        
class B(A):
    def __init__(self):
        self.x=20
    def getx(self):
        print("X : "+str(self.x))
        
        
obj=B()
obj.getx()