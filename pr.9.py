import math
a=int(input('dati primul numar:'))
b=int(input('dati al doilea numar:'))
c=int(input('dati al treilea numar:'))
def triunghi():
    global a,b,c
    if ((a+b>c) and (a+c>b)and (b+c>a)):
      p=a+b+c
      sp=p/2
      aria=math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
      h1=(2*aria)/a
      h2=(2*aria)/b
      h3=(2*aria)/c
      print('inaltimea a=',h1)
      print('inalimea b=',h2)
      print('inaltimea c=',h3)
    if ((a+b>c) or (a+c>b) or (b+c>a)):
        print('numerele nu corespund conditiei')
    return
print(triunghi())