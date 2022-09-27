x=int(input('primul numar:'))
y=int(input('al doilea numar:'))
z=int(input('al treilea numar:'))
#numarul maxim
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
#numarul minim
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
#cel mai mare divizor comun
def divizor(a,b,c):
    q=0
    for i in range(1,min(a,b,c)):
        if a%i==0 and b%i==0 and c%i==0: 
            q=i 
    return q
print('cel mai mare divizor comun', divizor(x,y,z))
#cel mai mic multiplu comun
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
#toti divizorii comuni 
def divizori_comuni(a,b,c):
    m=[]
    n=[]
    p=[]
    for i in range (1,a+1):
        if (a%i==0):
            m.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            n.append(j)
    for k in range (1,c+1):
        if (c%k==0):
            p.append(k)
    d=set(m).intersection(n)
    e=set(d).intersection(p)
    f=list(e)
    return f
print('toti divizorii comuni ai numerelor sunt: ', divizori_comuni(x,y,z))
#cei mai mici 3 multipli comuni
def multipli_comuni(a,b,c):
    m=[]
    if a>b:
        mlt=a
    elif b>a:
        mlt=b
    else:
        mlt=a
    while len(m)<3:
        if ((mlt%a==0)and(mlt%b==0)):
            m.append(mlt)
            mlt +=1
        else:
            mlt +=1
    return m
print('cei mai mici 3 multipli comuni al numerelor  sunt: ',multipli_comuni(x,y,z))
#verificam daca laturile pot fi leungimile unu triunghi
def triunghi(a,b,c):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
        t='numerele pot fi lungimile triunghiului'
    else:
        t='numerele nu pot fi lungimile triunghiului'
    return t
print(triunghi(x,y,z))
#aria triunghiului(formula lui Herone)
def aria(a,b,c):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
        s=(a+b+c)/2 
        A=(s*(s-a)*(s-b)*(s-c))**0.5   
    else:
        A='numerele nu pot fi lungimile triunghiului'
    return A
print('aria triughiului',aria(x,y,z))
#perimetrul triunghiului
def perimetru(a,b,c):
    if ( (a+b>c) and (b+c>a) and (a+c>b) ):
        p=a+b+c
    else:
        p='numerele nu pot fi lungimile triunghiului'
    return p
print('perimetrul',perimetru(x,y,z))
#ax^2+bx+c=0
def ecuatie(a,b,c):
    if a!=0:
        d=(b**2)-(4*a*c)
        if d>0:
            x1=(-b-(d**0.5))/(2*a)
            x2=(-b+(d**0.5))/(2*a)
        elif d==0:
            x1=x2=(-b)/(2*a)
        else:
            x1=x2='ecuatia data nu are solutii'
    else:
        x1=x2='ecuatia data nu are solutii'
    return x1,x2
print('ecuatia are solutiile solutii:',ecuatie(x,y,z))