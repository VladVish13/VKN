import math
k = input("Введіть значення сторін квадрату:  ")
l = input("Введіть координати точки x:  " )
h = input("Введіть координати точки y: ")
j = float(k)/2
g = float(k)/2

if float(l) > float(j):
    j = float(k)/2
    print("Точка не належить квадрату")
elif float(h) > float(j): 
    j = float(k)/2
    print("Точка не належить квадрату")
elif float(l) < float(j) or float(l) == float(j):
    j = float(k)/2 
    print("Точка належить квадрату")
elif float(h) < float(j):
    j = float(k)/2 
    print("Точка належить квадрату")
else :
    print("Точка не належить квадрату")
