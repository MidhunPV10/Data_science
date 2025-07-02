class Person:
    def setvalue(self,first_name,last_name,age,gender,phno):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.phno=phno

    def printvalue(self):
        print(self.first_name,self.last_name,self.age,self.gender,self.phno)

person1=Person()
person1.setvalue('Midhun','P V',23,'Male',949698)
person1.printvalue()

person2=Person()
person2.setvalue('Vinay','T',25,'Male',12345)
person2.printvalue()

person3=Person()
person3.setvalue('Adhi','S',20,'Male',123456)
person3.printvalue()

person4=Person()
person4.setvalue('Vijay','R',30,'Male',1234578)
person4.printvalue()

person5=Person()
person5.setvalue('Anjana','S',24,'Female',1234543)
person5.printvalue()