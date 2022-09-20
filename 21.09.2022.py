n=int(input('primul număr:'))
m=int(input('al doilea număr:'))
#suma numerelor
def suma(x,y):
    s=0
    s=x+y
    return s
print('suma numerelor:', suma(n,m))
#produsul numerelor
def produs(x,y):
    p=0
    p=x*y
    return p
print('produsul numerelor:', produs(n,m))
#media aritmetică a numerelor
def media_aritmetica(x,y):
    ma=0
    ma=(x+y)/2
    return ma
print('media aritmetica:', media_aritmetica(n,m))
#cel mai mare divizor comun
def divizor(x,y):
    w=[]
    z=[]
    for i in range (1,x+1):
        if (x%i==0):
            w.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            z.append(j)
    s=0
    mx=0
    s=set(w).intersection(z)
    mx=max(s)
    return mx
print('cel mai mare divizor comun:',divizor(n,m))
#cel mai mic multiplu comun
def cel_mai_mic_multiplu(x,y):
    mt=0
    c=0
    if x>y:
        mt=x
    elif x>y:
        mt=y
    else:
        mt=x
    while True:
        if ((mt%x==0)and(mt%y==0)):
            c=mt
            break
        mt +=1
    return c
print('cel mai mic multiplu comun:', cel_mai_mic_multiplu(n,m))
#numărul minim
def minim(x,y):
    if x<y:
        return x
    if y<x:
        return y
print('numarul minim:', minim(n,m))
#numărul maxim
def maxim(x,y):
    if x<y:
        return y
    if y<x:
        return x
print('numarul maxim:', maxim(n,m))
#a+b=c
def suma_2(x,y):
    s=0
    s=x+y
    return s
print('suma numerelor:',n,'+',m,'=', suma_2(n,m))
#a*b=c
def produs_2(x,y):
    p=0
    p=x*y
    return p
print('produsul numerelor:',n,'*',m,'=', produs_2(n,m))
#toți divizorii comuni
def divizori(x,y):
    c=0
    h=0
    k=[]
    l=[]
    for i in range (1,x+1):
        if (x%i==0):
            k.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            l.append(j)
    c=set(k).intersection(l)
    h=list(c)
    return h
print('divizorii comuni:', divizori(n,m))
#5 multipli comuni
def cinci(x,y):
    cm=[]
    if x>y:
        multiplu=x
    elif x>y:
        multiplu=y
    else:
        multiplu=x
    while len(cm)<5:
        if ((multiplu%x==0)and(multiplu%y==0)):
            cm.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return cm
print('multipli comuni:', cinci(n,m))
#cifrele care se conțin în ambele numere
def cifre_comune(x,y):
    c=0
    r=0
    p=[]
    t=[]
    for i in str(x):
        p.append(int(i))
    for a in str(y):
        t.append(int(a))
    c=set(p).intersection(t)
    r=list(c)
    if len(r)!=0:
        return r
print('cifrele comune:', cifre_comune(n,m))
#cifrele care sunt in primul număr și nu sunt în al doilea
def cifre_diferite(x,y):
    c=0
    r=0
    p=[]
    t=[]
    for i in str(x):
        p.append(int(i))
    for a in str(y):
        t.append(int(a))
    c=set(p).difference(t)
    r=list(c)
    return r
print('cifrele care se contin in primul numar si nu se contin in al doilea:',cifre_diferite(n,m))
#'PRIETENI', dacă nr de divizori este același
def acelasi_nr_divizori(x,y):
    t=[]
    p=[]
    for i in range (1,x+1):
        if (x%i==0):
            t.append(i)
    for a in range (1,y+1):
        if (y%n==0):
            p.append(a)
    if len(t)==len(p):
        print("nr sunt PRIETENE")
    else:
        print("nr nu sunt PRIETENE")
    return
print(acelasi_nr_divizori(n,m))