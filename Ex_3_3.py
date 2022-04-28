# square, cube
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = list(map(lambda x: x*x, lista))
cube = list(map(lambda x: x*x*x, lista))
print(square)
print(cube)