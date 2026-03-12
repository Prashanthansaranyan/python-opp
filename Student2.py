class Student2:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id

    def getfullname(self):
        return self.fname + self.lname

    def display(self):
        print("My fname is : " + self.fname)
        print("My lname is : " + self.lname)
        print("My id is : " + str(self.id))
        print("My full name is : " + self.getfullname())

stu = Student2("saran", "yan", 1000)
stu.display()