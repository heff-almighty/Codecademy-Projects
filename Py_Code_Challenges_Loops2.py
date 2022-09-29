#Larger Sum

#Define the function to accept two input parameters: lst1 and lst2
#Create two variables to record the two sums
#Loop through the first list and add up all of the numbers
#Loop through the second list and add up all of the numbers
#Compare the first and second sum and return the list with the greater sum


def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1:
    sum1 += i
  for i in lst2:
    sum2 += i
    
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
  
#####
  
#Define the function to accept a list of numbers
#Create a variable to keep track of our sum
#Iterate through every element in our list of numbers
#Within the loop, add the current number we are looking at to our sum
#Still within the loop, check if the sum is greater than 9000. If it is, end the loop
#Return the value of the sum when we ended our loop

def over_nine_thousand(lst):
  lst_sum = 0

  for i in lst:
    lst_sum += i
    if (lst_sum > 9000):
      break
  return lst_sum

#####

#Max Num

#Define the function to accept a list of numbers called nums
#Set our default maximum value to be the first element in the list
#Loop through every number in the list of numbers
#Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
#Return the maximum number

def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
  return maximum

#####

#Same Values

#Define our function to accept two lists of numbers
#Create a new list to store our matching indices
#Loop through each index to the end of either of our lists
#Within the loop, check if our first list at the current index is equal to the second list at the current index. 
#If so, append the index where they matched
#Return our list of indices

def same_values(lst1, lst2):
  lst3 = []
  for i in range (len(lst1)):
    if lst1[i] == lst2[i]:
      lst3.append(i) 
  return lst3

#####

#Reversed List

#Define a function that has two input parameters for our lists
#Loop through every index in one of the lists from beginning to end
#Within the loop, compare the element in the first list at the current index against the 
#element at the second list’s last index minus the current index. If there was a mismatch, 
#then the lists aren’t reversed and we can return False
#If the loop ended successfully, then we know the lists are reversed and we can return True


def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True
