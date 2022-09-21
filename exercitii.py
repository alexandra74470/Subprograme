x=int(input('primul numar:'))
y=int(input('al doilea numar:'))
z=int(input('al treilea numar:'))
def max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print('numarul maxim',max(x,y,z))
def min(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c
print('numarul minim',min(x,y,z))
def divizor(a,b,c):
    z=0
    for i in range(1,min(a,b,c)):
        if a%i==0 and b%i==0 and c%i==0: 
            z=i 
    return z
print('cel mai mare divizor comun', divizor(x,y,z))
def multiplu(a,b,c):
    mt=0
    d=0
    if a>b and a>c:
        mt=a
    elif b>a and b>c:
        mt=c
    else:
        mt=c
    while True:
        if ((mt%a==0)and(mt%b==0)and(mt%c==0)):
            d=mt
            break
        mt +=1
    return d
print('cel mai mic muliplu comun:',multiplu(x,y,z))