#First Three Multiples

#Define the function header to accept one input parameter called num
#Print out 1 times num
#Print out 2 times num
#Print out 3 times num
#Return the value of 3 times num

def first_three_multiples(num):
  num1 = num * 1
  print(num1)
  num2 = num * 2
  print(num2)
  num3 = num * 3
  print(num3)
  return num3

### OR ###

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

#####

#Tip Calc

#Define the function to accept the total cost of the food called total and the percentage to tip as percentage
#Calculate the tip amount by multiplying the total and percentage and dividing by 100
#Return the tip amount

 def tip(total, percentage):
    return (total * prcentage) / 100
  
 #####

#Bond, James Bond

#Define the function to accept two parameters, first_name and last_name
#Concatenate the string ', ' on to the last_name
#Concatenate the first_name on to the result of the previous step
#Concatenate a space on to the result
#Concatenate the last_name again to the result
#Return the final string

def introduction(first_name, last_name):
  intro = last_name + ", " + first_name + " " + last_name
  return intro

### OR ###

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

#####

#Dog Years

#Define the function called dog_years to accept two parameters: name and age
#Calculate the age of the dog in dog years
#Concatenate the string with the dog’s name and age in dog years
#Return the resulting string

def dog_years(name, age):
  output = name + ", you are " + str(age * 7) + " years old in dog years"
  return output

### OR ###

def dog_years(name, age):
  return name+", you are "+str(age * 7)+" years old in dog years"

#####

#All Operations

#Define the function to accept four inputs: a, b, c, and d
#Print and store the result of a + b
#Print and store the result of c - d
#Print and store the first result times the second result
#Return the previous result modulo a

def lots_of_math(a, b , c, d):
  one = a + b
  print(one)
  two = c - d
  print(two)
  three = one * two
  print(three)
  four = three % a
  return four
