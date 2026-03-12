class Student3:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def setmarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
            
    def caltotal(self):
        tot=self.m1+self.m2+self.m3
        return tot
        
    def calaverage(self):
        ave=self.caltotal()/3
        return ave
        
    def getresult(self):
        ave=self.calaverage()
        if(ave>=75):
            re='A'
        elif(ave>=65):
            re='B'
        elif(ave>=55):  
            re='C'
        elif(ave>=35):
            re='s'
        else:
            re='F'
        return re
            
    def display(self):
        print("student name : "+self.name)
        print("student id : "+str(self.id))
        print("student marks1 : "+str(self.m1))
        print("student marks2 : "+str(self.m2))
        print("student marks3 : "+str(self.m3))
        print("student total markes : "+str(self.caltotal()))
        print("student average markes : "+str(self.calaverage()))
        print("student result : "+self.getresult())
        
stu = Student3("saran",1000)
stu.setmarks(90,70,80)
stu.display()
        
        