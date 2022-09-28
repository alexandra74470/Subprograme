import math
a=int(input('dati primul numar:'))
b=int(input('dati al doilea numar:'))
c=int(input('dati al treilea numar:'))
def triunghi():
    global a,b,c
    if ((a+b>c) and (a+c>b)and (b+c>a)):
      m1=0.5*(math.sqrt((2*b**2)+(2*c**2)-(a**2)))
      m2=0.5*(math.sqrt((2*a**2)+(2*c**2)-(b**2)))
      m3=0.5*(math.sqrt((2*b**2)+(2*a**2)-(c**2)))
      print('mediana a=',m1)
      print('mediana b=',m2)
      print('mediana c=',m3)
    if ((a+b>c) or (a+c>b) or (b+c>a)):
        print('numerele nu corespund conditiei')
    return
print(triunghi())