from random import randint
n=int(input('introduceti numarul de aruncari:'))
k=0
for i in range(n):
    l=randint(1,6)
    print(l)
    if l==6:
        k+=1
print(f'cifra 6 va aparea de {k} ori')