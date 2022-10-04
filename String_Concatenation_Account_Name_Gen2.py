"""
Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates 
the last three letters of each and returns them as a string.

Test your function on the provided first_name and last_name and save it to the variable temp_password.
"""

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  first_len = len(first_name)
  last_len = len(last_name)
  account_name = first_name[first_len-3:] + last_name[last_len-3:]
  return account_name

temp_password = password_generator(first_name, last_name)
print(temp_password)
