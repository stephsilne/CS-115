'''
CS 115, Inheritance Activity
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement missing sections of the Employee class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Employee(object):
    '''Write the constructor below. It should take in five arguments:
       - first_name (a string)
       - last_name (a string)
       - title (a string)
       - hours_per_week (an int)
       - hourly_rate (a float)
       All fields must be private. No error checking or type conversions
       are required.'''
    def __init__(self,first_name,last_name,title,hours_per_week,hourly_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__hours_per_week = float(hours_per_week)
        self.__hourly_rate = float(hourly_rate)

    '''Write a getter for hourly_rate.'''
    def get_hourly_rate(self):
        return self.hourly_rate

    '''Write a setter for hourly rate.'''
    def set_hourly_rate(self,hr):
        self.hourly_rate = hr

    '''Write a method called get_total_compensation.
       It returns the total amount of money an employee earns in a year.
       Assume that the employee works 50 weeks each year, with the remaining
       2 set aside for vacation.'''
    def get_total_compensation(self):
        return 50 * self.hours_per_week * self.hourly_rate

    def __str__(self):
        return 'Employee: %s %s\n  Title: %s\n  Hours per week: %d\n' \
               '  Hourly rate: $%.2f\n  Yearly compensation: $%.2f' % \
            (self.__first_name, self.__last_name, self.__title, \
             self.__hours_per_week, self.__hourly_rate, \
             self.get_total_compensation())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement missing sections of the Manager class. Manager should be a
' subclass of Employee.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Manager(Employee):  
    '''Write the constructor below. It should take in six arguments:
    - the first five are the same as in the Employee constructor
    - bonus_percent, a float >= 0. This attribute represents the percentage
      of the employee's yearly compensation that will be used to
      create the manager's annual bonus.'''
    def __init__(self,first_name,last_name,title,hours_per_week,hourly_rate,bonus_percent):
        Employee.__init__(self,first_name,last_name,title,hours_per_week,hourly_rate)
        try:
            self.__bonus_percent = float(bonus_percent)
        except:
            print('We have an error, no bonus')
            self.__bonus_percent = 0.0
        if bonus_percent < 0:
            print('Not a valid bonus')
            self.__bonus_percent = 0.0

    '''Override the method get_total_compensation.
    It returns the total amount of money the manager earns in a year, i.e.
    basic employee compensation + bonus.
    Your implementation should call get_total_compensation in class Employee.
    Note: If a manager's yearly compensation is $100,000 and the bonus_percent
          is 10 (ten), the total compensation will be 110,000.'''
    def get_total_compensation(self):
        return super().get_total_compensation() + ((self.bonus_percent / 100) * super().get_total_compensation())


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' A rudimentary test.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test():
        m = Manager("Greta", "Thunberg", "Climate Change Leader", 50, 20.0, 10.0)
        m.set_hourly_rate(m.get_hourly_rate() + 20) # she earned it 
        print(m) # This will call Employee.__str__ which will call Manager.get_total_compensation
                 # She's making 110,000.00 
