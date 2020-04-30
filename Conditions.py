#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:06:32 2020

@author: riteshtripathi
"""

#Conditionals
#Logical, TrueFalse, If, 
#3 == 3 /chec in console

#Boolean Expression
# x = 5
# y = 6
# print('is it less: ', x < y)
# #check for greater, != , <= , >=

#Logical Operators, combine two boolean operators
#True and True, logical here is 'and'
#'or'
#True and True = True
#true or false = True
#True and False = True

# var3, var4, var5 = 15, 20, 25

# print(var4 < 100 and var5 < 100) 

#Not True = False
#Not False = True
#var3, var4, var5 = 15, 20, 25
#print(not(var4 < 100 and var5 < 100))
#and rest...

#IF STATEMENT
# temp = int(input('Enter a number\n'))

# if temp > 30:
#     print('Wear shorts')
# elif temp <= 30 and temp > 20:
#     print('do not buy shorts')
# else:
#     print('too cold')

# #More on Strings
# my_string = 'python'
# # print(len(my_string))
# # #and we can access the characters
# # #indexes, i have done al those
# #another way of indcing is:
# letter = my_string[4]
# print(letter)

# #another data structure is called the 'list'
# #if you understand for string, you understand for list


#More on String
#to Upper Case
#my_string.upper
#and same for lower

# #Guess the word Game
# word = 'summer'

# guess = input('enter a word\n')
# guess.lower()

# if guess == 'summer':
#     print('yes its summer')
# elif guess == 'winter':
#     print('nope, its not winter')
# else:
#     print(guess.capitalize(), 'is not a season')
#guess.capitalize: whatever we put not related to season, whatever is the first letter, makes it capital..
#and concatenate with 'is not a season'

#SUMMARY: the new thing i have learnt is 'guess.captialzie'....

#***********************************************************************
#Practical Challenge
#Qns1: Write code that asks user input nos btn 1 and 5, the code will take the integer value and print..
#out string value. eg, user inputs 2, code will print two, reject any input that is not a number in taht range
# user = int(input('Enter a number\n\n'))
# if user == 1:
#     print('one')
# elif user == 2:
#     print('two')
# elif user == 3:
#     print('three')
# else:
#     print('out of range')
# #suppose instead of a number, a user puts string, it throws error, 
# #will check in future


#Qns2: Repeat previous tasks, user will give string vakue and code will return the integer value
#convert the string to lower case
# user = input("Enter a string\n")
# user = user.lower()
# if user == 'one':
#     print(1)
# elif user =='two':
#     print(2)
# else:
#     print('Out of range')

# #now suppose user puts a number, there will be no error thrown, why?


#Qns3
#Create a variable containing an integer btn 1 and 10, ask user to guess the number, 
#if they guess too high or too low, tell them they have not won
#tel them they have won, if the no is right

# secret = 3
# guess = input('Guess the number')

# #check if user input is a digit or not
# if guess.isdigit():
# #if user input is a digit, convert to an integer
#     guess = int(guess)
#     if guess == secret:
#         print('Your right')
#     elif guess > secret and guess <= 10:
#         print('YOU GUESSED IT TOO HIGH')
#     elif guess < secret and guess >= 1:
#         print('You guessed it too low')
#     else:
#         print("Out of range")
#         #above is an IF NESTED and Logical Operartor used
# #if guess is not a digit
# else:
#     print('thats not even a number ')

#Qns4
# #ask user to input names, check lenth, if its greater than 5, telll them their lenght is secret
# name = input('Please enter name')
# name_len = len(name)
# if name_len > 5:
#     print('your name contains', name_len, 'characters')
    
# else:
#     print('I am not telling you')
#     #what if user types a number
    
#Qns5
#ask the user for two int btn 1 and 20, if they both greater than 15, return their product
# #if only one is greater than 15 return their sum, if neither are greater than 15 return zero
# int1 = int(input('Enter a first number:>'))
# int2 = int(input('Enter a second number:>'))

# if int1 > 15 and int2 > 15:
#     print(int1 * int2)
# elif int1 > 15 or int2 > 15:
#     print(int1 + int2)
# else:
#     print(0)

#Qns6
#ask user for two int, swapthe contents of variables 
# #if var1 = 1 and var2 = 2, 
# #code runs var1 as 2 and var2 as 1
# int1 = int(input('enter first number:>'))
# int2 = int(input('enter second number:>'))

# print('before swapping int1 = ', int1, 'and int2 = ',int2 )

# int1, int2 = int2,int1#we are putting int1 = int2, and int2 = int1, in one line

# print('before swapping int1 = ', int1, 'and int2 = ',int2 )


#in other langauges
#a = 20
#b = 30
#temp = a
#a = b
#b = temp
#a

#so far we have covered, boolean expression, logical operators, if statements and strings 










