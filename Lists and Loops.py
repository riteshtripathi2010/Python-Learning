#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:04:09 2020

@author: riteshtripathi
"""

#Repitetive Tasks
#Thats what Loops will do
#For Loops
#While loop: untill a certain condition is met

# #For Loops
# for i in range(10):
#     print(i)
    
# #but i want to print on same line
# for i in range(10):
#     print(i, end=' ')
    
#various other parameters
# for i in range(1,10):
#     print(i, end = ' ')
    
#Using STEPS
# #numbers going from 4
# for i in range(0,101,4):
#     print(i, end = ' ')

#Going steps back
# for i in range(100,0,-1):
#     print(i, end = ' ')

#Other ways of using for loop instead of using range
#word = 'python'

# for i in word:
#     #print(i)
#     print(i, end = ' ')

#i is used in index value not for strings
# #when iterating using string or lists
# word = 'python'
# for char in word:
#     print(char, end = ' ')
    
    
    
#MORE ON VARIABLES
#Change value of variable + loop
# x = 5
# #x = x +1
# print('x = ', x)
# #other way of incrementing
# x += 1

    
#LISTS
#So far we been using variable with one variable
#But we want a variable with more numbers
#Lists is a data structure
#data = [53,76,25,98,56,42,69,81]
#data[:5]
    
# #Iterate a lists
# for num in data:
#     print(num, end = ' ')
    
# #Combination of For Loop and Lists
# total = 0
# for num in data:
#     total = total + num
# print('the sum is', total)
# #this is me who has used this function, i have created this function
# #python comes in with more inbuilt function  

# total = sum(data)
# print('total', total, end = ' ')

#find max number in positive integer values
# max = 0
#data = [3,5,2,7,9,23,45,74]

# for num in data:
#     if num > 0:
#         max = num
# print('MAx value is',max)
#if num is > 0, which is 3 > 0, max which was 0 becomes that num, 3
#if 5 is > 0, 
#i have skipped

#but if above numbers were negative values?
#we will check in later course
#python has in built function to find max number
#print('Max value,',max(data))

#how to use range function to access list variables
# my_list = [1,11,21,31,41,51]
# for i in range(6):
#     print(my_list[i])
    #to get the paired value, i+1
    
#Power of working lists and loops working together
#Bubble Sort, people have dedicated their career to this
#I have skipped the user defined function

#For sorting in built python
#print(sorted(data))

#Some Lists Method
#Common Lists Methods
# my_lists = [34, 76, 58]

# (my_lists.append(100))
# my_lists,remove(34)
# my_lists.#do this and all the functions wil be available


#While Loops
#a while loop goes through a loop untill a condition is or not true
# n = 10
# while n > 0:
#     print(n)
#     n = n-1
#     #while n is greater than 0, it will print n and then decrease n by 1 and then will check the condtion and it will continue

# #User input
# user = int(input('please enter age: '))
# ages = []
# while user > 0:
#     ages.append(user)
#     user = int(input('the next age:'))
    
# print('age is',ages)#click -1 to get out of the loop

#Counter
#i have skipped this, it shows unique way of while loop with new print style
#above, we used while loop to append integer values, 
#now we use while loop to append string values

#MODULUS
# %
#this gives remainder
#11 % 2 = 1
#10 %4 = 2

#FizzBuzz
#Skipped this class

#PRactical
#Qns1: Ask the user for two numbers btn 1 and 100, then count from lower number to the higher
#print
# num1 = int(input("Enter first number:>"))
# num2 = int(input("Enter second number:>"))

# while num1 < 0 or num2 < 0 or num1 > 100 or num2 > 100 or num1 == num2:
#     print("Numbers should be different")
#     num1 = int(input("Enter first number:>"))
#     num2 = int(input("Enter second number:>"))

# if num1 < num2:
#     for i in range (num1,num2+1):
#         print(i,end = ' ')
# else:
#     for i in range(num2,num1+1):
#         print(i,end = ' ')

#Qns2
#Ask the user to input a string and print it out to the sceeen in reverse order

#word = input("Enter a string:")
# reverse = ''
# for char in word:
#     reverse = char + reverse
    
# print(reverse)
    
#another way of doing it
#print(word[::-1])

#Qns3
#ask the user for a no between 1 and 12 and then display a times tables for taht number
#i have skipped
#there are 10 qns





























  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
