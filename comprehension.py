celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [element*9/5 + 32 for element in celsius]

print(fahrenheit)


single_digits = range(0, 10)
squares = []

for single in single_digits:
    print(single)
    squares.append(single**2)

print(squares)

cubes = [single**3 for single in single_digits]

print(cubes)
