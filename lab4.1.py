import math

x = float(input("Введіть x "))
y = math.pow(x-4, 3)+math.log1p(x)/abs((x+math.cos(x))/(math.sin(x))) + math.pow(math.cos(x+2), 3)



print(y)