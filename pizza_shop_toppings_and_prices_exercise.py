# Your code below:
#Create toppings list

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#cost per slice 

prices = [2, 6, 1, 3, 2, 7, 2]

#count the number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#len of toppings list
num_pizzas = len(toppings)
print(num_pizzas)

#print string displaying number of pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#2D list with toppings and prices
pizza_and_prices = [
  [prices[0], toppings[0]], 
  [prices[1], toppings[1]], 
  [prices[2], toppings[2]], 
  [prices[3], toppings[3]], 
  [prices[4], toppings[4]],
  [prices[5], toppings[5]],
  [prices[6], toppings[6]],
  ]

#sort by price (lowest to highest)
pizza_and_prices.sort()
print(pizza_and_prices)

#select first in list as cheapest
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#select last in list as most expensive
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#remove anchovies from list
pizza_and_prices.pop()
print(pizza_and_prices)

#add new item at position 5
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#slice 3 cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
