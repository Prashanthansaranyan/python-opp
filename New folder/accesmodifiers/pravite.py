class Student1:
	
	def __init__(self,name,id):
		self.__name=name
		self.__id=id
	def display(self):
		print("My name is : "+self.__name)
		print("My id is :"+str(self.__id))
		
stu=Student1("saran",1000)
stu.display() 
stu1=Student1("maran",2000)
stu1.display()       