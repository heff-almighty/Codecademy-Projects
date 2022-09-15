single_digits = range(10)
squares = []

#loop method to square iterated items
for i in single_digits:
  print(i)
  squares.append(i**2)
  print(squares)

#list comprehension method to cube iterated items
cubes = [i ** 3 for i in single_digits]
print(cubes)
