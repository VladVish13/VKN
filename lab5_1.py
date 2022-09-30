import math 
x=float(input("Введіть х: "))
def f1(x1):
    vir=math.log2(3*x) - 7 * math.sqrt(x) 
    return(vir)
def f2(x2):
    vir=math.e**x + 2*x**3
    return(vir)
def f3(x3):
    vir=math.e**x + math.sin*(math.fabs(x + math.pi/4))
    return(vir)
y=0.0
if x > 5.1 or x == 5.1:
    y=f1(x)
if x > -0.7:
    y=f2(x)
if x< -0.7:
    y=f3(x)
print(y)