import random
n1=random.randint(1,999)
n2=random.randint(1,999)
b=random.randint(2,9)
#1. VERIFICA DACA BUN NR ESTE SCRIS CORECT IN SISTEMUL DE NUMERATIE CU BAZA B
def maxim(n):
    max=0
    while n>0:
        r=n%10
        n//=10
        if r>max:
            max=r
    return max

def verificare(n,d):
    elem=maxim(n)
    if elem<(d):
        return True
    else:
        return False   
#2. ADUNAREA NUMERELOR
def baza10(n,d):
        i=0
        s=0
        while n>0:
            r=n%10
            k=r*(d**i)
            n//=10
            s=s+k
            i=i+1
        return s

def suma(a,q,d):
    aa=baza10(a,d)
    bb=baza10(q,d)
    c=aa+bb
    return c

def convertirea_adunarea(a,q,d):
    sum=suma(a,q,d)
    list=[]
    while sum>0:
        nr=sum//d
        k=sum-(d*nr)
        list.append(k)
        sum=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Suma numerelor",n1,"si",n2,"in baza",b,"este:",final,'.')

#3 DIFERENTA
def diferenta_2_baze_10(a,q,d):
    aa=baza10(a,d)
    bb=baza10(q,d)
    if aa>bb:
        c=aa-bb
        return c
    elif bb>aa:
        c=bb-aa
        return c

def convertirea_scaderea(a,q,d):
    dif=diferenta_2_baze_10(a,q,d)
    list=[]
    while dif>0:
        nr=dif//b
        k=dif-(d*nr)
        list.append(k)
        dif=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Diferenta numerelor",n1,"si",n2,"in baza",b,"este:",final,'.')

#4. INMULTIREA
def inmultirea(a,q,d):
    aa=baza10(a,d)
    bb=baza10(q,d)
    c=aa*bb
    return c

def convertirea_inmultirea(a,q,d):
    inm=inmultirea(a,q,d)
    list=[]
    while inm>0:
        nr=inm//d
        k=inm-(d*nr)
        list.append(k)
        inm=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Inmultirea numerelor",n1,"si",n2,"in baza",b,"este:",final,'.')



print("Primul nr:",n1)
print("Al doilea nr:",n1)
print("Baza numerelor:",b)

if (b>1) and (b<10):
    print("Rezultatul verificarii bazei numarului",n1,"este:",verificare(n1,b))
    print("Rezultatul verificarii bazei numarului",n2,"este:",verificare(n2,b))
    if verificare(n1,b) and verificare(n2,b) :
        convertirea_adunarea(n1,n2,b)
        convertirea_scaderea(n1,n2,b)
        convertirea_inmultirea(n1,n2,b)