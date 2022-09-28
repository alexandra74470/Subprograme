import math
a=int(input('dati primul numar:'))
b=int(input('dati al doilea numar:'))
c=int(input('dati al treilea numar:'))
d=int(input('dati al patrulea numar:'))
def triunghi():
    global a,b,c,d
    if ((a+b>c) and (a+c>b)and (b+c>a)):
      p=a+b+c
      sp=p/2
      aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
      print('penru a=',a,'b=',b,'c=',c, ' perimeru=',p,' aria=',aria)
    if ((a+b>d) and (a+d>b)and (b+d>b)):
      p=a+b+d
      sp=p/2
      aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-d))
      print('penru a=',a,'b=',b,'d=',d, ' perimeru=',p,' aria=',aria)
    if ((d+b>c) and (d+c>b)and (b+c>d)):
      p=d+b+c
      sp=p/2
      aria=math.sqrt(sp*(sp-d)*(sp-b)*(sp-c))
      print('penru d=',d,'b=',b,'c=',c, ' perimeru=',p,' aria=',aria)
    if ((a+d>c) and (a+c>d)and (d+c>a)):
      p=a+d+c
      sp=p/2
      aria=math.sqrt(sp*(sp-a)*(sp-d)*(sp-c))
      print('penru a=',a,'d=',d,'c=',c, ' perimeru=',p,' aria=',aria)
    else:
        print('numerele nu corespund conditiei')
    return
print(triunghi())