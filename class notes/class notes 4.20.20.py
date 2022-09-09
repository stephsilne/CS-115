from cs115 import*

class Date(object):

    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year


    def __str__(self):
        '''returns string repres. for the object of type Date'''

        return '%2d/%02d/%04d' % (self.month,self.day,self.year)


    def isLeapYear(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

##
##class Student:
##    '''a student has a name (immutable), favorite color (mutable) and some grades.'''
##
##    def __init__(self, nameString,colorString):
##        self.___name = nameString
##        self.__faveColor = colorString
##        self.__grades = []
##
##    def getName(self): return self.__name
##
##    def getFaveColor(self): return self.__faveColor
##
##    def setFaveColor(self, colorString): self.__faveColor = colorString
##
##    def __str__(self):
##        return 'Student' + self.__name + 'who likes' + self.__faveColor
##
##    def __repr__(self):
##        return self.__str__()
##    
##    def addGrade (self,score):
##        self.__grades += [score]
##
##    def getGrades(self): return self.__grades
##
##alice = Student('Alice','red')
##bob = Student('Bob','blue')
##
##bob.setFaveColor(alice.getFaveColor())
##
##print('Bob now likes ' + bob.getFaveColor())
##
##alice.addGrade(100)
##alice.addGrade(80)
##bob.__grades = [0,0]
##
##
##print('Alices grades' + str(alice.getGrades()))
##
##agrade = alice.getGrades()
##agrade[1] = 50
##print('Alices changes grades!' + str(alice.getGrades()))


class Point:
    def __init__(self,InputX,InputY):
        self.x = InputX
        self.y = InputY
    def __repr__(self):
        return " " + str(self.x) + "," + str(self.y) + ")"
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self,Point1, Point2):
        self.Point1 = Point1
        self.Point2 = Point2
        self.slope = (Point1.y - Point2.y)/(Point1.x-Point2.x)
        pass
    


class Person:
    def __init__(self,first,last):
        self.firstName = first
        self.lastName = last

    def asleep (self,time):
        return 0 <= time <= 7

    def __repr__(self):
        return self.firstName + " " + self.lastName


class Student(Person):
    def __init__(self,first,last,age):
        Person.__init__(self,first,last)
        '''when referring to a function call for a class, do class.function, this can
            be donw within the same class as well, i.e. Line.parallel(self,other)'''
        
        self.age = age
    def asleep(self,time):
        return 3 <= time <= 11
    def __repr__(self):
        return Person.__repr__(self) + ", " + str(self.age) + " years old"


def add(x,y):
    x + y



def loop(N):
    n = None
    for i in range(N):
        add(4,3)
        
        




























