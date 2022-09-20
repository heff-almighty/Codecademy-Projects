# Write your code below: 
#define the function
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  #create variable to total car rental cost
  car_rental_total = car_rental_rate * trip_time
  #create variable to total accommodation cost
  hotel_total = hotel_rate *trip_time - 10
  #sum and print total cost 
  print(car_rental_total + hotel_total + plane_ticket_price)

# call the function
calculate_expenses(200, 100, 100, 5)
