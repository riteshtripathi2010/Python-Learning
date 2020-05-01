#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:29:07 2020

@author: riteshtripathi
"""

#so far we have covered
#avriables
#under variables: float, integer etc
#decision making using conditions, boolean values, logical operators, if statements
#looked into for loops
#looked into while loops
#and combining them with those conditions
#we have looked at data structures
#lists
#dicitionaries
#files and create own functions
#everything in python is an OBJECT

#OBJECTS
#x = 1
#what objects do they combine data with functions

#
##help(x)
##dir(x)

##
#y = [1,2,3]#lets create lists
##help(y)
##dir(y)
#lets append 5 to the list
# y.append(5)
# print(y)


##
#z = {'a':1}#this is a dictionary
#help(z)
#dir(z)
#so far we been dealing with objects
#we append to a data: this is a function on a data used

#we can write/create our own object with the help of CLASS

#Class
#classes are the blueprint of the objects
#we have to decide what data is that object going to store 
#and then we that in a class
#then we have to decide what functions we have to manupilate 
#what data we have to put in the class
#and when we finish desiginng the blue print inside the class
#we can then intanitate the object of that class which holds the information
#so the class is the design
#and the object is what we built using that design

#you have a medical practise
# #you want to keep track of the patients
# class Patient(object):
#     ''' Medical centre patient'''
#     pass
# #above code will not crash because it doesnt have any codes written in it
# x = Patient()
# x
# #x will display the memory location 

# x.name = 'Steven'
# x.age = 30

# x.name
# #this will reuslt int he name steven
 
# class Patient(object):
#     ''' Medical centre patient'''
    
#     def __init__(self,name,age):#this is a function inside this class Patient
#     #this is a very special function inside a class
#     #this creates variables that contain values for each instance of above object 
#     #so that different instances have different variables associated to it
#     #def _in... is called a constructor 
#     #it initializes these variables and takes arguments there, 
#     #arguments are: self, name, age
#     #self: we dont know the name of the object that this class is going to create
#     #thats down to the user
    
        
#         self.name = name
#         self.age = age
#     #here self.name creates variable name
#     #here self.age creates variable age
#     #into which we put these values, where object,name,age values will go to the variables created by self
#     #those variables are created by the above constructor
#     #therefore each instance of object will have different values

# #now when we run it/call it, this will ensure that each instance will have unique value for these variables
# #now we create instance saved variable for Steve 
# steve = Patient('Steven Hughes',48)
# #now we look at the name value and the age value
# print(steve.name)

# print(steve.age)

# #lets create another object now
# abigail = Patient('Abigail Sandwick',32)
# #now lets look at the instance variables
# print(abigail.name)

# print(abigail.age)

# #therefore we have two instances of Patient Class that are holding their own data
# #and they are holding in their variable names
# #which are created by the constructor: def __init__(self,name,age)
# #and they are unique to each instance that we create

#Class Variables
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age #these are instance variables that are created by the above constructor

#METHODS
#we need to interact with the data that we have created
#and to that we are going to neeed a FUNCTION 
#because this function is inside the class, its called a METHOD
#that is accessible through the 'dot notation'
#this FUNCTION is created just like the other function but with just one diff, 'SELF'
# #lets create another function:
# class Patient(object):
#     ''' Medical centre patient'''
    
#     status = 'patient'
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
        
#     def get_details(self):
#         print(f'Patient record: {self.name}, {self.age} years.')
#     #this function will display patient details on the screen

# steve = Patient('Steven Hughes',48)
# abigail = Patient('Abigail Sandwick',32)

# #now run these commands on the output screen
# steve.get_details()
# #it would print: Patient Record: 'Steve HUghes', 48 years

#so this method is enabling us to interact with method variables that we have created for this particular object
#the last part of Method, quite confusing, left it out

#Inheritance
#inheritance creates new classes that are derived from other classes
#these new classes becomes the child classes from the parent class that they are derived from
class Patient(object):
     ''' Medical centre patient'''
     
     status = 'patient'
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions}.')
         
     def add_info(self,information):
         self.conditions.append(information)
#     
#
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)

#here we have created another class for patients below 2 years called INFANTS
#Infant here is inheriting from the patient class
#this infant class doesnt have a "Class Variable'
#it does have _init_ function
#a new variabel name called self.vaccination is set to empty lists

# class Infant(Patient):
#     ''' Patient under 2 years'''
    
#     def __init__(self,name,age):
#         self.vaccinations = []
#         super().__init__(name,age)
# #in the above function we have 'super()' which is a function 
# #which searches the parent class for the command 'init_(name,age)
# #above line is initilazing from the parent class
# #therefore int his infant class we are deriving variables from parent class
# #and creating a new variable too
# #thereofre we have name, age, conditions and vaccination variables

# #point to note, why we set vaccination to empty its because, 
# #later we would get details from user as vaccoination the infant had is MMR
# #and this MMR will get saved into this vaccination variable
        
#     def add_vac(self,vaccine):
#         self.vaccinations.append(vaccine)
# #above is the new instance method called add_vacc, which is the list of vaccination that the infant has had

        
#     def get_details(self):
#          print(f'Patient record: {self.name}, {self.age} years.' \
#                f' Patient has had {self.vaccinations} vaccines.' \
#                f' Current information: {self.conditions}.' \
#                f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
# #above is the same function that we had in parent class, but here we have ammended it


# #now lets create a new instance of the infant class        
# archie = Infant('Archie Fittleworth',0)        
# #lets now add archie.add_vac('MMR')
# archie.add_vac('MMR')

# #then lets get detaisl on this variable
# archie.get_details()


#The above code without explanation goes like this

# class Patient(object):
#      ''' Medical centre patient'''
     
#      status = 'patient'
     
#      def __init__(self,name,age):
#          self.name = name
#          self.age = age
#          self.conditions = []
         
#      def get_details(self):
#          print(f'Patient record: {self.name}, {self.age} years.' \
#                f' Current information: {self.conditions}.')
         
#      def add_info(self,information):
#          self.conditions.append(information)
# #     
# #
# #steve = Patient('Steven Hughes',48)
# #abigail = Patient('Abigail Sandwick',32)

# class Infant(Patient):
#     ''' Patient under 2 years'''
    
#     def __init__(self,name,age):
#         self.vaccinations = []
#         super().__init__(name,age)
        
#     def add_vac(self,vaccine):
#         self.vaccinations.append(vaccine)
        
#     def get_details(self):
#          print(f'Patient record: {self.name}, {self.age} years.' \
#                f' Patient has had {self.vaccinations} vaccines.' \
#                f' Current information: {self.conditions}.' \
#                f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
        
#archie = Infant('Archie Fittleworth',0)        
#archie.add_vac('MMR') 

#now i know how to use classes to create our own object 
#these objects can work with their own data and variables
#and they can create functions/methods
#we mention method, because the functions are inside a class
#this is called Object Orient Programming
#what Object Orient Programming do: 
    #is to create object that have their own data and their own methods
    #and they can interact with each other
    #and it can simplyfy more complex programmes
    
#Practical
'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods 
work as expected.
'''
# class BankAccount(object):

#     def __init__(self,balance=0.0):
#         self.balance = balance
    
#     def display_balance(self):
#         print(f'Your balance is {self.balance}')

# #below is another method 
#     def make_deposit(self):
#         amount = float(input('How much would you like to deposit?:> '))
#         self.balance += amount#this line updates that value to user input
#         print(f'Balance is now {self.balance}.')

# #below method checks if there is enough balance
#     def make_withdrawal(self):
#         amount = float(input('How much would you like to withdraw?:> '))
#         if amount > self.balance:
#             print(f'You do not have sufficient funds, your balance is {self.balance}')
#         else:
#             self.balance -= amount#this line will deduct
#             print(f'Withdrawal successful: balance is now {self.balance}.')
            
#Now lets insantiate now, all these codes should be in OUTPUT PANE
#my_bank = BankAccount(300)#lets start with balance of 100
#print(my_bank.display_balance())

#my_bank.make_deposit()#check the result in the output

#my_bank.make_withdrawal()
#by typing the code in this pane, will cause some errors, its better to type in the output pane

#lets withdraw more mooney
#my_bank.make_withdrawal()


'''
Question 2
 Create a circle class that will take the value of a radius and 
 return the area of the circle
'''
import math

class Circle(object):
    ''' Represents a circle with radius. Calculates area.'''
    
    def __init__(self,radius):
        self.radius = radius
        
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area

#lets instantiate
#ar_circle = Circle(8)#here 8 is raidus, but run in output pane

#lets calcualte
#ar_circle.calc_area()



































































































