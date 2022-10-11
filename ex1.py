from random import randint
n=int(input('dati numarul de cifre:'))
Spoz=0
Sneg=0
for i in range(n):
    k=randint(-50,50)
    if k>0:
        Spoz+=k
    if k<0:
        Sneg+=k
print(f'Spoz={Spoz},Sneg={Sneg}')