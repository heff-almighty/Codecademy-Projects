#####

#DIV BY 10

#Define the function to accept one input parameter called nums
#Initialize a counter to 0
#Loop through every number in nums
#Within the loop, if any of the numbers are divisible by 10, increment our counter
#Return the final counter value

def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 ==0:
      counter = counter +1
  return counter
  
#####
  
  #GREETINGS
  
#Define the function to accept a list of strings as a single parameter called names
#Create a new list of strings
#Loop through each name in names
#Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
#Afterwards, return the new list of strings

def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list
  
#####

#Delete Starting Even Numbers

#Define our function to accept a single input parameter lst which is a list of numbers
#Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
#Within the loop, if the first number in the list is even, then remove the first number of the list
#Once we hit an odd number or we run out of numbers, return the modified list

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
  
#####
  
#ODD INDICES
 
#Define the function header to accept one input which will be our list of numbers
#Create a new list which will hold our values to return
#Iterate through every odd index until the end of the list
#Within the loop, get the element at the current odd index and append it to our new list
#Return the list of elements which we got from the odd indices.

def odd_indices(lst):
  new_lst = []
  for i in range(1, len(lst), 2):
    new_lst.append(lst[i])
  return new_lst
  
#####

#Exponents

#Define the function to accept two lists of numbers, bases and powers
#Create a new list that will contain our answers
#Create a loop that iterates through every base in bases
#Within that loop, create another loop that iterates through every power in power
#Within that nested loop, append the result of the current base raised to the current power.
#After all iterations of both loops are complete, return the list of answers

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
  
