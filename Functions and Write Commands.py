#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:05:45 2020

@author: riteshtripathi
"""
#Files and Functions
#write a code and bring that code whenever i need it
#File Handling
#File Handling can Open, Close, Read, Write

#f = open('kipling.txt','w') #even if this file isnt created, it will still open it
#the w is for writing in the file
#print(type(f))

# #Writing first to file
# f.write('If you can keep your head while all about you \nare losing theirs\
# #and blaming it on you,\n')

# f.write('If you can trust yourself when all men doubt you,\n\
# But make allowance for their doubting too;\n')
# #
# f.write('If you can wait and not be tired by waiting,\n\
# Or being lied about, don\'t deal in lies,\n')
# #
# f.write('Or being hated, don\'t give way to hating,\n\
# And yet don\'t look too good, nor talk too wise:\n')
# #
# f.close()

#now check the file 'kipling' is in the file explorer

#Now lets Read the file
# f = open('kipling.txt','r')
# print(type(f))
# #   
# print(f.read())
# f.close()

#if you want to handle line by line, then there is this readLine command
# f = open('kipling.txt','r')

# print(f.readline())
# f.close()
# print() #this will give you the first line of the text

# f = open('kipling.txt','r')
# #
# print(type(f))
# #
# content = f.readlines()#i have stored in the variable because i want to iterate and find line by line
# f.close()

# #Appendto a file
# f = open('kipling.txt','a')
# f.write('If you can dream - and not make dreams your master;\n\
# If you can think - and not make thoughts your aim;\n')
# f.close()#after appending, we need to close the file
# print()
# #this will append from the last line

# #then we need to read that file with the new line
# f = open('kipling.txt','r')
# print(f.read())
# f.close()
# print()



#FUNCTIONS
#Some built in function in Python: MIn, Max, Sum

#lets use our own custom function called Modular Programming / Few Errors
#Wriitng your function makes programming more modular and it reduces potential errors

#Print Hello World function
# def Hello():
#     print('Hello World')
#     #i have created a function called hello, and it will not run unless i call it
# Hello()

# for i in range(5):
#     Hello()#this will print the function 5 times
    
# #A function can take an argument
# def hi(name):
#     print(f'Hello, {name}!')    
 
# #here name is an input
# #lets call the function
# hi('Ritesh')
# #i can pass varibales to a function
# #in above, if i dont pass in any name, python will throw error
# #to solve that, check the code below

# def hi_2(name='Ritesh'):
#     print(f'Hello, {name}!')
# hi_2()
# #if i dont pass any parameter, by default, hi_2 will take as Ritesh


#Fibonacci Sequence in a FUNCTION
#Normally for Fibonacci, we could write code as below
# n=20
# a = 0
# b = 1
# for i in range(n):
#     a,b = b,a+b
# print(a)   

#now lets write above code in a function and we dont have to write that code ever
# def fib(n):
#     #''' Calculates and returns the nth fibonacci number'''
#     a = 0
#     b = 1
#     for i in range(n):
#         a,b = b,a+b
#     return a
 
# fib_num = fib(20)
# print(fib_num)
    
# for i in range(20):
#     print(fib(i))
#  #this will calculate finonacci series from 1 to 20   
 

# #lets create another function
# def calc_mean(first,*remainder):
#     '''
# #    This calculates the mean of numbers.
# #    '''
#     mean = (first + sum(remainder))/ (1 + len(remainder))
#     print(type(remainder))
#     return mean
    
# print(calc_mean(23,43,56,76,45,34,65,78,975,3456,54))
# # Docstring: with three ''' lets other user to knwo what this function is doing
# #above, *remainder tells python we dont know how many inputs we are going to get, handle it
# #in short, * can handle whatever lenght we give to the function, it can handle

#Recursion
# #in a fucntion you can call the function by itself and its called Recursion
# #Recursion can create memory drainage
# def fib_2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_2(n-1) + fib_2(n-2)
# #All recurscive functions need base case, they need to resolve for something or else it will keep running forever
# #here base case is 0 and 1, it will keep checking for 0 and 1, as soon as it equals to 0 and 1
# #it will not call any functions
# #untill these base case have gone to more than 1 
# x = fib_2(20)
# print(x) 
    
#skipped more on fibonnaci numbers like a min video, 
#because using recursion method takes fib function to execute in 25mins
#iterative function is less by 25mins faster

#so far we have created three function and all those functions are saved under one file called 
#Files and Functions

#i can open FIles and Functions in other page by calling that file name and then dot to access each function
# #Eg
# import FilesandFunction
# x = FilesandFunctions.fib(20)
#this is called MODULE


#More on Functions
#A function can return more than one value
#its done by tuple of values

# def sum_and_mult(a,b):
#    total = a + b
#    product = a * b
   
#    return total, product
# #above returns sum and product of two values
# #lets call the function
# func_call = sum_and_mult(3,4)

# print(func_call)
# print(type(func_call))

# #another way of returning tuple values
# var_1, var_2 = sum_and_mult(6,7)
# #here var1 will return the addition of 6 and 7
# #here var2 will return the multiplication of 6 and 7

# #Another point to note, 
# #a variable declared outside the function will be differetn from the variables 
# #defined inside the function
# var_3 = 5
# var_4 = 6
# #
# def add1(var_3,var_4):
#     var_3 = var_3 + 1
#     var_4 = var_4 + 1
    
#     print(f'Inside the function var_3 = {var_3} and var_4 = {var_4}')
#     return var_3,var_4
# #
# add1(18,19)

# print(f'But outside the function var_3 = {var_3} and var_4 = {var_4}')
# #above code is self explanotary

# #another point to note
# #if you put mutable values inside the function, 
# #those values willlll change
# def lengthen_list(n,my_list = [1,2,3]):#here it takes values n and my_list
# #but if my_list hasnt been given value, by default it would be 1,2,3
#     my_list.append(n)
#     return my_list
# x = lengthen_list(4)
# #this is like the first call
# x = lengthen_list(4)
# ##this is like the second call
# x = lengthen_list(4)
# #this is like the third call

# #whats happening above is that, values 1,2,3
# #will get append first time by 4
# #the number of times x is shown, the value will keep appending
# #reuslts 1,2,3,4,4,4,
# #inshort everytime we call x, it will keep appending and we dont want that

# #rather we code:
# def lengthen_list_2(n,my_list = None):
#     if my_list == None:#checking the condition, if its true
#         my_list = [1,2,3]
#         my_list.append(n)
#         return my_list
# #y = lengthen_list_2(4)
# ##
# #y = lengthen_list_2(4)
# ##
# #y = lengthen_list_2(4)


#main thing to note, we need to define function before we call it
# def multi_ply(a,b):
#     return a * b
    
# p = multi_ply(3,4)


#Practical Tests
#Question 1
#Create a function that will calculate the sum of two numbers. Call it sum_two.

# def sum_two(a,b):
#     '''This function returns the sum of two numbers'''
#     return a + b
# print(f'The sum of 3 and 4 is {sum_two(3,4)}' )

# Question 2
# Write a function that performs multiplication of two arguments. By default the 
# function should multiply the first argument by 2. Call it multiply.
# def multiply(a,b=2):
    
#     '''
#     Returns the product of a and b; if b not given 
#     returns 2 * a.
#     '''
    
#     return a * b
# #
# print(f'Inputting 3 gives {multiply(3)}')
# print(f'Inputting 3 and 5 gives {multiply(3,5)}')

    

#Question 3
#Write a function to calculate a to the power of b. If b is not given
#its default value should be 2. Call it power.
#'''
# def power(a,b=2):
#     '''
#     Returns a**b; if b not given,
#     it will return a**2
#     '''
#     return a ** b

# print(f'Inputting 8 gives {power(8)}')
# print(f'Inputting 2 and 8 gives {power(2,8)}')


##Question 4
##Create a new file called capitals.txt , store the names of five capital cities
##in the file on the same line.
##'''
#file = open('capitals.txt','w')
#file.write('London, ')
#file.write('Paris, ')
#file.write('Madrid, ')
#file.write('Lisbon, ')
#file.write('Rome,')
#file.close()
    
    
#Question 5 
#Write some code that requests the user to input another capital city.
#Add that city to the list of cities in capitals. Then print the file to
#the screen.
#'''
#user_input = input('Plese enter a capital city:> ')
#
#file = open('capitals.txt','a')
#file.write('\n' + user_input)
#file.close
#
#file = open('capitals.txt','r')
#print(file.read())
#file.close


#Question 6
#Write a function that will copy the contents of one file to a new file.
# '''
# def copy_file(infile,outfile):
#     ''' Copies the contents of infile to a new file, outfile.'''

#     with open(infile) as file_1:
#         with open(outfile, "w") as file_2:
#             file_2.write(file_1.read()) 



# copy_file('capitals.txt','new_capitals.txt')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















































    




























































































