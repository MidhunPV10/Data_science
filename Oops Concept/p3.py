class Student:
    def details(self,id,f_name,l_name,course,gender,coll_name):
        self.id=id
        self.f_name=f_name
        self.l_name=l_name
        self.course=course
        self.gender=gender
        self.coll_name=coll_name

    def printvalue(self):
        print(self.id,self.f_name,self.l_name,self.course,self.gender,self.coll_name)

student1=Student()
student1.details('1','Midhun','PV','Data Science','Male','Jyothi')
student1.printvalue()

student2=Student()
student2.details('2','Ajith','T','Flutter','Male','Vidya')
student2.printvalue()

student3=Student()
student3.details('3','Ajay','S','Python','Male','Gec')
student3.printvalue()

student4=Student()
student4.details('4','Abel','cp','Mern','Male','Jyothi')
student4.printvalue()

student5=Student()
student5.details('5','Abhinav','R','Python','Male','Gec')
student5.printvalue()