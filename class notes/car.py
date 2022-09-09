'''
CS 115, Lab 12, Inheritance

Author: Stephaan Silne
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self,make,model,mpg,tank_capacity):
        '''initializes all fields, for the class Car to expect'''
        self.__make = make
        '''initializes make as a field of the calling object, privately'''
        self.__model = model
        '''initializes model as a field of the calling object, privately'''
        self.__mpg = mpg
        '''initializes mpg as a field of the calling object, privately'''
        self.__tank_capacity = tank_capacity
        '''initializes tank_capacity as a field of the calling object, privately'''
    '''Write getters for make, model, mpg, and tank_capacity.'''

    def get_make(self):
        '''obtains the 'make' field'''
        return self.__make
        '''returns make'''
    def get_model(self):
        '''obtains the make field'''
        return self.__model
        '''returns model'''
    def get_mpg(self):
        '''obtains the 'mpg' field'''
        return self.__mpg
        '''returns mpg'''
    def get_tank_capacity(self):
        '''obtains the 'tank_capacity' field'''
        return self.__tank_capacity
        '''returns tank_capacity'''

    '''Write setters for mpg and tank_capacity.'''

    def set_mpg(self,p):
        '''sets mpg to user choice of float p'''
        self.__mpg = p
        '''initializes mpg field to p'''
    def set_tank_capacity(self,t):
        '''sets tank_capacity to user choice of float t'''
        self.__tank_capacity = t
        '''initializes tank_capacity field to t'''

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        '''returns the total distance the car can travel on a full tank of
       gas'''
        return self.__mpg * self.__tank_capacity
        '''multiplies the mpg field by the tank_capacity field'''


    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self,make,model,mpg,tank_capacity,battery_kWh,miles_per_kWh):
        '''initializes all 6 arguements to passed around as field for other methods'''
        Car.__init__(self,make,model,mpg,tank_capacity)
        '''initializes the first four arguments through subclassing Car and accessing the init method'''
        self.__battery_kWh = battery_kWh
        '''initializing battery_kWh to be a field of self'''
        self.__miles_per_kWh = miles_per_kWh
        '''initializing miles_per_kWh to be a field of self'''
        
    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return (self.__battery_kWh * self.__miles_per_kWh)
        '''returns the multiplication of the battery_kWh and the miles_per_kWh for total battery range'''

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        '''overridden version of get_total_range from the Car class'''
        return super().get_total_range() + self.get_battery_range()
        '''references get_total_range from the previous class and adds it to the total battery range'''
    
    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
