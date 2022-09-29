#Tenth Power

#Create a function that raises numbers to the tenth power


def tenth_power(num):
  i = num ** 10
  return i

#####

#Square Root
#Create a function that returns the square root of a number

def square_root(num):
  return num ** 0.5

#####

#Win Percentages

#Define the function header with two parameters, wins and losses
#Calculate the total number of games using the number of wins and losses
#Get the ratio of winning using the number of wins out of the total number of games.
#Convert the ratio to a percentage
#Return the percentage

def win_percentage(wins, losses):
  win_percent = float(wins / (wins + losses))
  return win_percent * 100

#####

#Average

#Define the function with two input parameters, num1 and num2
#Calculate the sum of the two numbers
#Divide the sum by the number of inputs to the function
#Return the answer

def average(num1, num2):
  return (num1 + num2) / 2

#####

#Remainder

#Define the function to accept two parameters
#Multiply the first input value by 2
#Divide the second input value by 2
#Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
#Return the answer

def remainder(num1, num2):
  a = num1 * 2
  b = num2 * 0.5
  c = a % b
  return c

### OR ###

def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

