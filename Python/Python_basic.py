#Python programming basics
import os
import sys
import random
print("following the python course by Edureka - https://www.youtube.com/watch?v=vaysJAMDaZw&t=782s ")
print("=======================================")

#Functions
def fun1(ar1, ar2):   #fun definiton. ar1 and ar2 are arguements. fun1 is the name of function.
    s=ar1+ar2
    return s

print (fun1(10,20))  #prints 30

print("=======================================")

#Lambda functions 
#helps to make functions more concise, quick and easy to write
#these functions cannot contain commands and must have only 1 expression (but can take any number of arguements including optional arguements)
#defined useing keyword 'lambda'

a=(lambda x:x*x)  # syntax = (lambda input:output)
print(a(2)) #prints 4  Notice that a is called like a function

#map
l1=[1,2,3,4]
b=list(map(lambda x:x**2,l1)) #prints [1,4,9,16] squares each item in l1. 'map' here applies lambda fn on each element of l1.
print(b)

print("=======================================")

#Control statements in a loop
#break - breaks out of the loop completely and executes the next line after the loop
#continue - skips the reminder of the loop body and goes back to the start of next loop(provided loop condition is met)
#pass - when a statement is required syntatically but no code is to be executed (can be used when code block is not completed and we dont want the program to break.)

print("=======================================")

#File I/O
#Writing to a file
test_file=open('test.txt', 'wb')
print(test_file.mode) #prints wb
print(test_file.name) #prints test.txt
test_file.write(bytes("This is a test file.\n"))
test_file.close()

#Reading and writing to a file
test_file=open("test.txt", "r+")  #r+ to read and write both
data = test_file.read()
print(data)

#rename a file
os.rename("test.txt","test1.txt")

#remove the file
os.remove("test1.txt")

print("=======================================")


#OBJECTS

class Test1():
    def __init__(self):
        self.__privateVar = "I am private variable." #double __ represents private variable
        self._protectedVar = "I am protected variable" #single _ represents protected variable
        self.publicVar = "I am public variable"
    
    def __privateMethod(self):
        print("In private method")
    
    def _protectedMethod(self):
        print("In protected method")
    
    def publicMethod(self):
        print("In public method")
    
obj1=Test1()
print(obj1.publicVar)  #prints the public variable
print(obj1._protectedVar) # prints the protected variable 
#print(obj1.__privateVar)  #Throws error as private var cannot be accessed directly. There is a way to access, see below
print(obj1._Test1__privateVar) #prints the private variable

obj1.publicMethod()  # accesses public method
obj1._protectedMethod()  #accesses protected method
#obj1.__privateMethod() #Throws error as private method cannot be accessed directly.
obj1._Test1__privateMethod() #accesses private method

print("=======================================")

print("=======Class variables and instance variables=======")

class Test2():
    classVar = "I am a class variable"
    def method1(self,instanceVar):
        self.instanceVar = instanceVar
        print(instanceVar)

obj2 = Test2()
obj3 = Test2()

print(obj2.classVar) #I am a class variable
print(obj3.classVar) #I am a class variable

obj3.classVar="I am a class variable modified by obj3"
print(obj3.classVar) #I am a class variable modified by obj3
print(obj2.classVar) #I am a class variable

obj2.method1("instance variable for obj2") #instance variable for obj2
obj3.method1("instance variable for obj3") #instance variable for obj3

print("=======================================")

print("=======Constructor and Destructor=======")
class Test3():
    def __init__(self):
        print("In Constructor. Constructing the obj by initializing some values")
    
    def __del__(self):
        print("In Destructor. Destroying the obj...")
    
    def method1(self):
        print("in method1")

obj4=Test3() # In Constructor. Constructing the obj by initializing some values

obj4.method1() #in method1
obj4.__del__() #In Destructor. Destroying the obj...   <DOES not actually delete the obj>
obj4.method1() #in method1

del obj4 #In Destructor. Destroying the obj... <THIS time obj is deleted>
#obj4.method1() #error as obj4 no longer exists

print("=======================================")

print("=======Multiple Constructors=======")
#Used when a class is requried to be initialized in different ways.
class Date1():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        print("YMD format")

    @classmethod  #to tell the class that the below method is an alternate constructor
    def dmy(cls, day, month, year):  #cls is like self
        cls.day = day
        cls.month = month
        cls.year = year
        print("DMY format")
        return cls(cls.year, cls.month, cls.day) #order of return should be same as init
    
    @classmethod
    def mdy(cls, month, day, year):
        cls.month = month
        cls.day = day
        cls.year = year
        print("MDY format")
        return cls(cls.year, cls.month, cls.day)
obj5 = Date1(2019,4,21)
print(obj5.year)
obj6 = Date1.dmy(20,3,2018)
print(obj6.year)  #note that the print in init is also executed after the print in dmy
obj7 = Date1.mdy(3,24,2020)
print(obj7.year)  ##note that the print in init is also executed after the print in mdy

print("=======================================")

print("=======Simple Inheritance=======")  #NOT Fully Clear. Need more practice!!
class Test4():
    def m1(self):
        print("In parent m1")
class subTest4(Test4):
    pass #nothing to do here
class sub2Test4(Test4):
    def m1(self):
        print("In sub2 m1")

o1 = subTest4()
o1.m1() # IN parent m1
o2 = sub2Test4()
o2.m1() # In sub2 m1  ....if the same method exists in sub class, that takes precedence over the method in parent class.

class Test7():
    def __init__(self):
        print("In Test7")
class subTest7(Test7):
    #def __init__(self):
        #super().__init__()
     #   print("In subTest7")
     pass
o3=subTest7()

print("=======================================")

print("=======Multiple Inheritance=======")  #NOT Fully Clear. Need more practice!!
class Test5(object):  #code does not work without 'object' being passed....why is that??
    def __init__(self):
        super(Test5, self).__init__()
        print("First")
class Test6(object):
    def __init__(self):
        super(Test6,self).__init__()
        print("Second")
class subMulti(Test5,Test6):   #inherits from both Test5 and Test6
    def __init__(self):
        super(subMulti,self).__init__()
        print("Third")
o8=subMulti()


print("=======================================")

print("=======Inheritance Again=======")



#Class
class Animal():
    __name=""    #__ before the name makes the attributes private.
    __height=0
    __weight=0
    __sound=0

    def __init__(self, name, height, weight, sound):    #constructor - used to initialize the values when an object of the class is created.
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound 


    def set_name(self, name):  # 'self' allows an object to refer to itself(i.e. the class) from inside the class
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_height(self, height):
        self.__height = height
    
    def get_height(self):
        return self.__height
    
    def set_weight(self, weight):
        self.__weight = weight
    
    def get_weight(self):
        return self.__weight
    
    def set_sound(self, sound):
        self.__sound = sound
    
    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")
    
    def toString(self):
        return "{} is {} cm tall and weighs {} kilos and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

lion = Animal('Rocky', 50, 15, 'Woof')

print(lion.toString())


#Inheritance
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner #only the new attribute need be defined, rest of the attributes can be sent to the super class constructor
        Animal.__init__(self, name, height, weight, sound)
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("Dog")
    
    def toString(self):  #Funtion overriding (when same funtion name exists in super and sub class, the sub class function takes precedence)
        return "{} is {} cm tall and weighs {} kilos and says {} and the owner is {}".format(self.get_name(), self.get_height(), self.get_weight(),
        self.get_sound(),self.get_owner())
    
    #Function overloading
    def multiple_sounds(self, how_many=None):    #the attribute how_many may or may not be sent... if not sent print soud once, if sent print sound as many times as told. 
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)

spot = Dog("spot", 60, 12, "Woof", "Tester")

print(spot.toString())
print(spot.multiple_sounds(3))
