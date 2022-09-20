import math
def func111 (x, y, z):
        
        R= int( 12 * (x**2+ (math.sin(y))) + (math.sqrt(math.pow(z, 2) + (1)) / (math.log(abs(z)+0.07, 3))))
        return(R)

x=float(input("Введіть першу змінну: "))
y=float(input("Введіть другу змінну: "))
z=float(input("Введіть третю змінну: "))
d=func111 (x,y,z)
print(d)

