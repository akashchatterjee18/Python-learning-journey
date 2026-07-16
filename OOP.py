#OOPS

# Creating Class
class Student:
    name = "Ayush"
# Creating Object
s1=Student()
print(s1)
print(s1.name)


# Another-One
class Car:
    color = "Blue"
    brand = "Mercedes"

car1= Car()
print(car1)
print(car1.color)
print(car1.brand)


# Constructor (__init__ function)
class Officers:
    name = "Shreyas Iyer"
    def __init__(self):
        print("adding new officer to database:")

o1 = Officers()
print(o1.name)


class Officer:
    def __init__(self,name,marks):
        #print(self)
        self.name=name
        self.marks=marks

o2=Officer("Karan",94)
print(o2)    # same as print(self)
print(o2.name) # Karan
print(o2.marks) # 94

o3=Officer("Arjun",95)
print(o3)
print(o3.name)
print(o3.marks)

"""
Attributes : Any Data (name,marks,etc)
two types : class attr and instances(object) attr

Class Attr
Class.attr same for all obj in the class
eg : clg name when working on data of students of same clg

Object Attr
Obj.attr diff for diff obj in the class
eg : student name
"""

class Officerx:
    institution = "IB"
    def __init__(self,name,marks):
        #print(self)
        self.name=name
        self.marks=marks

o4=Officerx("Panther",94)
print(o4)
print(o4.name,o4.marks,o4.institution)


o5=Officerx("Leo",95)
print(o5)
print(o5.name,o5.marks,o5.institution)

"""
here, name and marks are obj.attr
while, institution is class.attr
"""

print(Officerx.institution)
print(o4.institution,o5.institution,Officerx.institution) # same result IB


# METHODS
"""METHODS are function that belong to objects"""
"""creating class"""
class Studentx:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("hello",self.name)
"""creating object"""
s10 = Studentx("Fafa")
s10.hello() # print hello Fafa


"""
PRACTICE 1 : Create student class that takes name and marks of 4 subjects
as arguments in constructor. then create a method to print the average.
"""
"""creating class"""
class Practice:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("hello",self.name,"your avg score is:", sum/4)
"""creating object"""
s10 = Practice("Fafa",[58,58,58,58])
s10.avg()


#STATIC METHOD : DON'T USE SELF PARAMETER
class W:
    @staticmethod   #decorator
    def clg():
        print("ku")
"""
decorators allow us to wrap another function in order to
extend the behavior of the wrapped function without
permanently modifying it.
"""

"""
PRACTICE 2 :Create Account class with 2 attributes - balance and account no.
create methods for debit, credit and printing the balance
"""
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total balance =",self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total balance =",self.get_balance())
    #get balace
    def get_balance(self):
        return self.balance
acc1 = Account(10000,123456)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(2000)




# ABSTRACTION : Hiding the implementation details (unnecessary) of a class and only showing the essential features to the user.
class CARS:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started..")
car1 = CARS()
car1.start()

# ENCAPSULATION : Wrapping data and functions into a single unit (object).
# INHERITANCE : When one class(child/derivative) derives the properties and methods of another class(parent/base)
"""
class Car:
    .........
class ToyotaCar(Car):
    .........

three types of inheritance
1. single
2. multi-level
3. multiple
"""

# 1. single inheritance
class Cars:
    color = "black"
    @staticmethod
    def start():
        print("car started.....")
    @staticmethod
    def stop():
        print("car stopped.....")
class ToyotaCar(Cars):
    def __init__(self,name):
        self.name = name

car10 = ToyotaCar("fortuner")
car20 = ToyotaCar("prius")
print(car10.name)
print(car20.name)
print(car10.start())
print(car10.stop())
print(car20.color)


# 2. multi level inheritance

class Carx:
    color = "black"
    @staticmethod
    def start():
        print("car started.....")
    @staticmethod
    def stop():
        print("car stopped.....")
class ToyotaCarx(Carx):
    def __init__(self,brand):
        self.brand = brand
class fortuner(ToyotaCarx):
    def __init__(self,type):
        self.type = type

car100 = fortuner("diesel")
car200 = fortuner("petrol")
car300 = fortuner("electric")
car100.start()

# 3. multiple inheritance
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B): # inherting from multiple parents
    varC = "welcome to class C"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#super method() used to access methods of the parent class
class Cary:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started.....")

    @staticmethod
    def stop():
        print("car stopped.....")

class ToyotaCary(Cary):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()
car105 = ToyotaCary("prius","electric")
print(car105.type)



# POLYMORPHISM : explained below



"""
DEL Keyword : used to delete object properties or object itself.
eg. del s1.name
del s1
"""


"""
Private(like) attributes and methods:
Conceptual Implementation in Python:-
Private attributes and methods are meant to be used only within the class
and are not accessible from outside the class.
"""


class Studenta:
    def __init__(self,name):
        self.name=name

s1= Studenta("shraddha") #public attribute
print(s1.name)

class Accounts:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass     #private attribute
    def reset_pass(self):
        print(self.__acc_pass)
acc10 = Accounts("12345","abcde")
print(acc10.acc_no)
#print(acc10.__acc_pass)  # Error
print(acc10.reset_pass())



"""
 class method : #decorator
it is bound to the class and recieves the class as an implicit first argument.

note : static methos can't access or modify class state and generally for utility.
"""

class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)






class Personx:
    name = "anonymous"

    def changeName(self, name):
        Personx.name = name

p1 = Personx()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Personx.name)






class Persony:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = "AB"

p1 = Persony()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Persony.name)




class Personz:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Personz()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Personz.name)



# Property : decorator

class Studentxyz:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    #def calcpercentage(self):
     #   self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"


st1= Studentxyz(98,97,99)
print(st1.percentage)

st1.phy = 86
print(st1.phy)
print(st1.percentage)



# Polymorphism : when same operator is allowed to have different meanings acc to the context
print(1+2) #3
print("akash"+" "+"chatterjee") #concatenate
print([1,2,3]+[4,5,6]) #merge
#all of these are implicit overloading ie. with different datatypes the operator will behave differently
class complex:
    def __init__(self,real,img):
       self.real = real
       self.img = img
    def showno(self):
        print(self.real,"+",self.img,"i")
    def add(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal,newimg)

num1 = complex(1,3)
num1.showno()
num2 = complex(4,6)
num2.showno()
num3 = num1.add(num2)
num3.showno()

"""
Dunder function (starts with double underscore)
# add  a.__add__(b)    means a + b
# subtract  a.__sub__(b)    means a - b
"""

class Complex:
    def __init__(self,real,img):
       self.real = real
       self.img = img
    def shownum(self):
        print(self.real,"+",self.img,"i")
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)
    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal,newimg)
num4 = Complex(7,3)
num4.shownum()
num5 = Complex(2,2)
num5.shownum()
num6 = num4+num5
num6.shownum()
num7 = num4-num5
num7.shownum()




"""
DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS R USING THE CONSTRUCTOR.
DEFINE AN AREA() METHOD OF THE CLASS WHICH CALCULATES THE AREA OF THE CIRCLE.
DEFINE A PERIMETER() METHOD OF THE CLASS WHICH ALLOWS YOU TO CALCULATE THE PERIMETER OF THE CIRCLE.
"""
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        return 3.14*self.radius**2
    def Perimeter(self):
        return 2*3.14*self.radius

c1 = Circle(21)
print(c1.Area())
print(c1.Perimeter())

"""
DEFINE A EMPLOYEE CLASS WITH ATTRIBUTES ROLE, DEPARTMENT AND SALARY.
THIS CLASS ALSO HAS A showDetails() METHOD.
CREATE AN ENGINEER CLASS THAT INHERITS PROPERTIES FROM EMPLOYEE AND HAS ADDITIONAL ATTRIBUTES : NAME AND AGE
"""


class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetails(self):
        print("role =", self.role)
        print("department =", self.dept)
        print("salary =", self.sal)


emp1 = Employee("accountant","finance","50000")
emp1.showDetails()


class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("name =", self.name)
        print("age =", self.age)
        super().__init__("Engineer","IT","75000")

engg1 = Engineer("Elon Musk", "50")
engg1.showDetails()
