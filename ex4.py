from random import randint
nr1=randint(1,6)
nr2=randint(1,6)
while nr1!=nr2:
    nr1=randint(1,6)
    nr2=randint(1,6)
print(f'numerele aruncate sunt {nr1} si {nr2}')
print(f'suma numerelor duble este {nr1+nr2}')