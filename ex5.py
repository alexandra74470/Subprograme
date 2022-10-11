from random import randint
n=int(input('dati numarul de elemente:'))
l=[]
suma=0
for i in range(n):
    l.append(randint(1,100))
for i in l:
    if i!=max(l):
        suma+=i
print(l)
print(suma)