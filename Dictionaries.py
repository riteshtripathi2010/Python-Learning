#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:45:35 2020

@author: riteshtripathi
"""

# #Dictionaries
# #Standard Python Libraries
# #Inbuilt functions
# # #Math Module
# # import math
# # print(math.pi)
# # math.cos(0)

# #Random Module
# # import random #as r
# # #Selecting random integers
# # print(random.randint(1,100))

# # #Using for loop
# # for i in range(100):
# #     print(random.randint(1,100), end = ' ')
    
# # import webbrowser 
# # webbrowser.open('')

# #Dictionaries: a new datastructures in python
# #they are different from lists, lists are ordered
# #Dictironaries are not ordered
# #Dictionary is very fast, has KEY and VALUE pairs
# #Dictionaries: consists of KEY VALUE pairs
# #LISTS: a sequential collection of items

capitals = {'FRANCE':'Paris', 'INDIA':'DELHI', 'KENYA':'NAirobi'}
# #above is a key value pair
# #The rule is that you cant change, it is immutable
# #immutable: strings, numbers, 
# #not immutable: lists
# #good thing with dictrionaries: keys could be accessed quickly
# #and they are not ordered
# #if you get 1000 key value pairs, you will get keys quickly

# print(capitals['INDIA'])
# #another way
# capitals.get('INDIA')

# #to add new value in dictionaries
# capitals['South Korea'] = 'Seoul'
# capitals

# #to check all the remaining functions:
#     #capital. (and check all the functions)

# print(capitals.items())
# #we will cover tuple soon

# for country in capitals:
#     print(country)
#     #this has iterated in ..i forgot the world
    
# #to iterate (Key Value pairs) with names assigned to them:
# for country, city in capitals.items():
#     print(f'The capital of {country}, is {city}')       
    
#we can iterate using key
#print(capitals.keys())
#this prints all keys

#print only values
#print(capitals.values())

#therefore we can extract in dictionaries: 
    #items
    #keys
    #values
    #we can also check if particular item is there in dictionaries
# if 'FRANCE' in capitals:
#     print('it contains FRANCE')

#we can also check if a particular item is in a list
# l = [1,2,3,4,5]
# print(7 in l)#this will result in boolean expression

#now we know what dict and how they work
#lets analyse some text
#Dict are a great way to store and analyse data
# sherlock = '''
# Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table. I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. It was a fine, thick piece of wood, bulbous-headed, of the sort which is known as a “Penang lawyer.” Just under the head was a broad silver band nearly an inch across. “To James Mortimer, M.R.C.S., from his friends of the C.C.H.,” was engraved upon it, with the date “1884.” It was just such a stick as the old-fashioned family practitioner used to carry—dignified, solid, and reassuring.

# “Well, Watson, what do you make of it?”

# Holmes was sitting with his back to me, and I had given him no sign of my occupation.

# “How did you know what I was doing? I believe you have eyes in the back of your head.”

# “I have, at least, a well-polished, silver-plated coffee-pot in front of me,” said he. “But, tell me, Watson, what do you make of our visitor’s stick? Since we have been so unfortunate as to miss him and have no notion of his errand, this accidental souvenir becomes of importance. Let me hear you reconstruct the man by an examination of it.”

# “I think,” said I, following as far as I could the methods of my companion, “that Dr. Mortimer is a successful, elderly medical man, well-esteemed since those who know him give him this mark of their appreciation.”

# “Good!” said Holmes. “Excellent!”

# “I think also that the probability is in favour of his being a country practitioner who does a great deal of his visiting on foot.”

# “Why so?”

# “Because this stick, though originally a very handsome one has been so knocked about that I can hardly imagine a town practitioner carrying it. The thick-iron ferrule is worn down, so it is evident that he has done a great amount of walking with it.”

# “Perfectly sound!” said Holmes.

# “And then again, there is the ‘friends of the C.C.H.’ I should guess that to be the Something Hunt, the local hunt to whose members he has possibly given some surgical assistance, and which has made him a small presentation in return.”

# “Really, Watson, you excel yourself,” said Holmes, pushing back his chair and lighting a cigarette. “I am bound to say that in all the accounts which you have been so good as to give of my own small achievements you have habitually underrated your own abilities. It may be that you are not yourself luminous, but you are a conductor of light. Some people without possessing genius have a remarkable power of stimulating it. I confess, my dear fellow, that I am very much in your debt.”

# He had never said as much before, and I must admit that his words gave me keen pleasure, for I had often been piqued by his indifference to my admiration and to the attempts which I had made to give publicity to his methods. I was proud, too, to think that I had so far mastered his system as to apply it in a way which earned his approval. He now took the stick from my hands and examined it for a few minutes with his naked eyes. Then with an expression of interest he laid down his cigarette, and carrying the cane to the window, he looked over it again with a convex lens.
# '''

#Count how many instances there are of each letter in this text
#we create a for loop
#initially i am having letter_count empty

# letter_count = {}
# for letter in sherlock:
#     letter_count[letter.lower()] = letter_count.get(letter,0) + 1
    
# print(letter_count)    #hard to visualize, hence lets use matplotlib

# import matplotlib.pyplot as plt
# x,y = zip(*letter_count.items())
# #here zip has taken all the key value pairs from dict and unpacked them here
# #
# plt.bar(x,y)
# plt.show()
#
#the last part i have missed it out, too heavy for me
#just a min video


#ZIP
# my_list_1 = [1,2,3,4]
# my_list_2 = ['a','b','c','d']

# joined = list(zip(my_list_1,my_list_2))
# print(f'The result of the zip function is {joined} it is of type {type(joined)}')
#its taking 1,a and so on, by taking the index positions same

#we have converted zip to List in above
#the remaining part of ZIP i have skipped, didnt feel like its part of my course

#More Strings
#SPLIT
#especially used in when cleaning data
#new_words = sherlock.split(' ')
#this will split every after word a space

#Strip another method
#i have skipped this, looking for an example for strip will be better to understand

#if you want to check if a word is in the variable, then..
#'sherlock' in new_variable, it will return TRUE

#TUPLES
# my_tuple = (1,2,3,4)
# my_list = [5,6,7,8]
# my_string = 'Australia'

# #a tuple is in different bracket as compared to a list and a string
# #to access an element of a tuple, just like list
# my_tuple[0]
# my_tuple[:3]#the first three elements

# #but there are things that i can do with list that cant be done with a tuple
# #i can change elements in LIST
# my_list[0] = 1000
# my_list

#i cant change values in a tuple
#cant change values in strings also
#my_string[4] = 2000, will throw error

#In Summary:
    # Lists are mutable
    # Dict are mutable
    # Tuples are immutable
    # Strings are immutable
#you use dict when you want to look things quickly
#like looking into facebook which has billion of users

#adding extra dimensions to a lists
#a list can contain a list
#a dictionary can conatain a dictionary
#my_list = [[1,2,3],[4,5,6],[7,8,9]]
#the first element above is 1,2,3, and index would be 0
#second element is 4,5,6, index is 1
#to access 5 number
#my_list[1][1],bse,1st element endex is 1 and 5 is indexed at 1 also

#lets look eg in dict
# countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
#             'United Kingdom':{'Capital':'London','Language':'English'},
#             'United States':{'Capital':'Washington DC','Language':'English'},
#             'Italy':{'Capital':'Rome','Language':'Italian'}
#             }
#above, value now is being a dictionary
#means: first value is France which is the key
#and value is a dictionary having Key Value
#lets acces the key of France
# print(countries['France'])

# #Displaying Key Value pairs
# for key, value in countries.items():
#     print(key,value)

# #iterating better
# for key, value in countries.items():
#     print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}.')
    
#above code is self explanotary

#therefore dictoanries are very important and they can be converted into dataframes later

#Import Counters
#there was some explanation in writing shorter code (Dict Comprehension), i skipped that, but learnt shorter code for list
#writing in one line
# L = [x**2 for x in range(1,11)]
# print(L)
# #above method is called list comprehension

# #normally we would write above code as: 
# M = []
# for x in range(1,11):
#     M.append(x**2)

#we learnt so far
#Modules
#Dict
#Zip Function
#String Methods
#Tuples
#Dict and Lists can have more than one dimensions

#Now lets put above to test, 
#last lecture of this
# Question 1
# Can you remember how to check if a key exists in a dictionary?
# Using the capitals dictionary below write some code to ask the user to input
# a country, then check to see if that country is in the dictionary and if it is
# print the capital. If not tell the user it's not there.
# '''

#capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#            }
#
#user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.lower()
#
#
#
#below we using united kingdom and united states because in our dict these two countries have space
#and rest of the countries are single word
#while ('united kingdom' not in user_input and not user_input.isalpha()):
#    if user_input == 'united states':
#        break
#    print('You must input a string')
#    user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.title()
##print(user_input)
#if user_input in capitals:
#    print(f'The capital of {user_input} is {capitals[user_input]}')
#else:
#    print('No data available') 

# Question 2
# Write python code that will create a dictionary containing key, value pairs
# that represent the first 12 values of the Fibonacci sequence 
# i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}    
'''
#n = 12
#a = 0 
#b = 1
#d = dict()
#for i in range(1,n+1):
#    d[i] = a
#    a,b = b,a+b
#print(d)  
#i have skiped 2nd question


# Question 3
# Create a dictionary to represent the open, high, low, close share price data 
# for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
# the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
# '''

#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#key_names = ['Open','High','Low','Close']
#prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
#d_1 = {}
#
#for i in range(len(key_names)):
#    d_1[companies[i]] = dict(zip(key_names,prices[i]))
#        
#print(d_1)    

#we are mapping open to 12.87, high to 13.23 etc..
#run the code you will understand

# Question 4
# Go to the python module web page and find a module that you like. Play with it, 
# read the documentation and try to implement it.
'''
## Days until holiday!
#import datetime
#
#today = datetime.date.today()
#
#print(f"Today's date is {today}")
#holiday = datetime.date(2019,12,25)
#delta = holiday - today
#
#print(f"Just {delta.days} days until the holidays!")

#just look at the code, easy to understand
#we are getting todays date and calculating how many days left from holiday of 25th dec from todays date


# Question 5
# Create a dictoinary containing as keys the letters from A-Z, the values should 
# be random numbers created from the random module. Can you draw a bar graph of 
# the results?
# '''

#import random
#
#keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#d = dict()
#
#for letter in keys:
#    d[letter] = random.randint(1,100), whats happening here,
#the first time d will be A and will be assigned value btn 1 to 100
#    
#print(d)    
#
#import matplotlib.pyplot as plt
#
#x,y = zip(*d.items()) 
#
#plt.bar(x,y)


# Question 6
# Create a dictionary containing 4 suits of 13 cards 
# ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# '''

# suits = ['Spades','Clubs','Hearts','Diamonds']
# rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

# deck = dict()

# for i in suits:
#     deck[i] = rank
    
# print(deck)    









































