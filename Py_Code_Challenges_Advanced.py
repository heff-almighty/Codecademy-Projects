#SMALL PROBLEMS USING FUNCTIONS

#EVERY 3 NUMBERS

#Create a function called every_three_nums that has one parameter named start.
#The function should return a list of every third number between start and 100 (inclusive). 
#For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
#If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  return list(range(start, 101, 3))

#######

#REMOVE MIDDLE

#Create a function named remove_middle which has three parameters named lst, start, and end.
#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#######

#MORE FREQUENT ITEM

#Define the function to accept three parameters: the list, the first item, and the second item
#Count the number of times item1 shows up in our list
#Count the number of times item2 shows up in our list
#If item1 shows up more, return item1. Otherwise, return item2

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
  
#######

#DOUBLE INDEX

#We will provide a list and an index to double. This will create a new list by replacing the value at the 
#index provided with double the original value. If the index is invalid then we should return the original list. 
#Here is what we need to do:

#Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
#Test if the index is invalid. If its invalid then return the original list
#If the list is valid then get all values up to the index and store it as a new list
#Append the value at the index times 2 to the new list
#Add the rest of the list from the index onto the new list
#Return the new list

def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    #generate new list and select a range to be iterated over
    new_lst = lst[0:index]
    #iterate over new list and double the index
    new_lst.append(lst[index]*2)
    #update new list with doubled index and everything after the index number
    new_lst = new_lst + lst[index+1:]
    #return new list
    return new_lst
  
#######

#MIDDLE ITEM 

#For the final code challenge, we are going to create a function that finds the middle item from a list of values. 
#This will be different depending on whether there are an odd or even number of values. 
#In the case of an odd number of elements, we want this function to return the exact middle value. 
#If there is an even number of elements, it returns the average of the middle two elements. 
#Here is what we need to do:

#Define the function to accept one parameter for our list of numbers
#Determine if the length of the list is even or odd
#If the length is even, then return the average of the middle two numbers
#If the length is odd, then return the middle number

def middle_element(lst):
  #determine if list is composed of an odd or even amount of items
  if len(lst) % 2 == 0:
    #algorithm to determine the middle index of the list
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    #divide the sum by 2
    return sum /2
  else:
    return lst[int(len(lst)/2)]
