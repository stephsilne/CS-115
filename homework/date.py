'''
@author:   Stephaan Silne
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
            as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''changes the calling object self to be one calendar day after the date originally given'''
        i = self.month
        '''initialize i to be the month of orig. date'''
        if self.day in range(DAYS_IN_MONTH[i]):
            '''if the day of the date in within the range of (0 - days in month of its respective month - 1)'''
            self.day += 1
            '''increase the day by 1'''
        elif Date(self.month,self.day,self.year).isLeapYear() and self.day == 28:
            '''otherwise if its a leap year and the day is the 28th (meaning is feb.28 on a leap year'''
            self.day += 1
            '''increase the date by 1'''
        elif self.month == 12 and self.day == 31:
            '''otherwise if the date is 12.31.year'''
            self.day = 1
            '''the day should be set to the first'''
            self.month = 1
            '''the month should be set to january'''
            self.year += 1
            '''and the year should be incremented into the next year'''
        else:
            self.day = 1
            '''otherwise if the date is the end of the month of any month other than dec., the day should be the first'''
            self.month += 1
            '''and the month should be increased by 1'''

    def yesterday(self):
        '''changes the calling object to be a calendar date before the original date given'''
        i = self.month
        '''initialize i to be the month of the origin. date'''
        if self.day in range(2,DAYS_IN_MONTH[i]+1):
            '''if the day in in the range of (2 - days in month of its respective month)'''
            self.day -= 1
            '''decrement the day'''
        elif Date(self.month,self.day,self.year).isLeapYear() and self.day == 29:
            '''otherwise if its a leap year and the date is feb. 29'''
            self.day -= 1
            '''decrement the day'''
        elif self.month == 1 and self.day == 1:
            '''otherwise if the date is jan.1'''
            self.day = 31
            '''the previous day should be the 31st'''
            self.month = 12
            '''the previous month should be december'''
            self.year -= 1
            '''and the year should be decremented'''
        elif self.month == 3 and self.day == 1 and Date(self.month,self.day,self.year).isLeapYear():
            '''otherwise if the date is march.1 and the year is a leap year'''
            self.day = 29
            '''the previous day should be the 29th'''
            self.month = 2
            '''and the prevous month should be feb.'''
        else:
            self.day = DAYS_IN_MONTH[i-1]
            '''otherwise if it is the first of any month, the day should be the last day of the previous month'''
            self.month -= 1
            '''and the month should be decremented'''

    def addNDays(self,N):
        '''adds n amount of days to the date given and prints each iteration'''
        print(self)
        '''prints the date given'''
        for i in range(N):
            '''for every iteration in N given'''
            self.tomorrow()
            '''call the tomorrow method onto self'''
            print(self)
            '''and print each change to self'''

    def subNDays(self,N):
        '''subtracts n amount of days from the date given and prints each iteration'''
        print(self)
        '''print the original date'''
        for i in range(N):
            '''for N amount of times'''
            self.yesterday()
            '''call the method yesterday onto self'''
            print(self)
            '''print each change to self'''
        

    def isBefore(self,d2):
        '''checks to see if self is before d2'''
        if self.year < d2.year:
            '''if the year of self is less than the year of d2, it is automatically before'''
            return True
            '''returns True for this case'''
        elif self.month == d2.month:
            '''otherwise if the months of each are the same'''
            if self.day < d2.day:
                '''if the day of self is less than d2's day'''
                return True
                '''return True as it is before d2'''
        elif self.year == d2.year:
            '''otherwise if they are in the same year'''
            if self.month < d2.month:
                '''if the month of self is before the month of d2'''
                return True
                '''return True as the date of self is before d2'''
        else:
            return False
            '''otherwise just return False'''
            

    def isAfter(self,d2):
        '''returns true if date of self is after d2'''
        if self.year > d2.year:
            '''if the year of self is after d2'''
            return True
            '''return True as it is automatically after d2'''
        elif self.month == d2.month:
            '''otherwise if they are in the same month'''
            if self.day > d2.day:
                '''if the day of self is greater or after d2'''
                return True
                '''return True'''
        elif self.year == d2.year:
            '''if they are in the same year'''
            if self.month > d2.month:
                '''if the month of self is greater of 'after' d2's month'''
                return True
                '''return True'''
        else:
            return False
            '''otherwise return False if no other cases are hit'''


    def diff(self,d2):
        '''computes self - d2, finding the number of days between the dates'''
        day1 = self.copy()
        '''creates copy of self as to not change the original date'''
        day2 = Date.copy(d2)
        '''creates copy of d2 as to not change the original date'''
        numdays = 0
        '''initializes numdays to 0 for iterations'''
        
        while day1.isBefore(day2):
            '''while day1 is before day2'''
            day1.tomorrow()
            '''keep calling the tomorrow function on day1 as to reach day2's date'''
            numdays -= 1
            '''and decrement numdays by -1 to show how many days before it is before day2'''
        while day1.isAfter(day2):
            '''while day1 is after day2'''
            day1.yesterday()
            '''keep calling the yesterday function onto day1 to reach day2's date'''
            numdays += 1
            '''increment numdays by 1 to show how many days after day1 is after day2'''

        return numdays
        '''return numdays'''
        

    def dow(self):
        '''returns the day of the week of date given'''
        DOW = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        '''initializes the tuple DOW containing all the days of the week for referencing'''
        d2 = Date(11,9,2011)
        '''initializes d2 to be 11.9.2011, a known date to be Wednesday'''
        do_w = DOW[2]
        '''initializes the current day of the week to be DOW[2] or Wednesday'''
        i = self.diff(d2)
        '''initializes i to be the function call to diff which returns self - d2'''
        i = i % 7
        '''computes %7 to i that was previously calculated to be the diff of days between self and d2'''
        try:
            i += 2
            '''adds 2 to i, so that the days of week starts off at wednesday'''
            do_w = DOW[i]
            '''after, do_w is set to the day of the week or DOW[i]'''
        except IndexError:
            '''if an index error occurs, such that i is too large'''
            i = i - 7
            '''decrement i by 7 as this will be the exact index of DOW to be the day of the week'''
            do_w = DOW[i]
            '''initializes do_w to be DOW[i]'''
        return do_w
        '''returns do_w to be the day of the week indexed at i'''

            
            
        
        

        

        
            
                
         
                
            
            













    
