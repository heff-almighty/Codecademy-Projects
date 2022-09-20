#Codecademy TripPlanner v1.0

#create welcome function
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 "+ name)

#call welcome function with your name passed as an argument
trip_planner_welcome("Simon")

#define function estimated_rounded_time with a single parameter: estimated_time
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

#create variable "estimate" and 
estimate = estimated_time_rounded(3.10)

#Generate messages for round trip:
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are travelling to " + destination)
  print("You will be travelling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

#call the above function with the assigned parameters
destination_setup("Dublin", "Mayo", estimate, )
