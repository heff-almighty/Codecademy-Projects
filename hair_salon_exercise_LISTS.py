hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#loop to tally prices into variable total_price
for i in prices:
  total_price += i
  
#set variable for average price
average_price = total_price / len(prices)
print("Average Haircut Price $", str(average_price))

#comprehension to change prices
new_prices = [i - 5 for i in prices ]
print(new_prices)

#Total revenue  calculation
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  print("Total Revenue: ", str(total_revenue)
  )

#average revenue finder
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#identify cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] <= 30]

print(cuts_under_30)
