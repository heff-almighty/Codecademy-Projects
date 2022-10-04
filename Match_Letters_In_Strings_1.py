"""
Function to match letters in strings
"""

def contains(big_strings, little_strings):
  return little_strings in big_strings

def common_letters(string_one, string_two):
  mutual = []
  for i in string_one:
    if (i in string_two) and not (i in mutual):
      mutual.append(i)
  return mutual
