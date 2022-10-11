from random import randint
k=[]
for i in range(1):
    l=randint(0,999999999)
    print(l)
while l>0:
    r=l%10
    l//=10
    k.append(r)
print(f'0 apare de {k.count(0)} ori')
print(f'1 apare de {k.count(1)} ori')
print(f'2 apare de {k.count(2)} ori')
print(f'3 apare de {k.count(3)} ori')
print(f'4 apare de {k.count(4)} ori')
print(f'5 apare de {k.count(5)} ori')
print(f'6 apare de {k.count(6)} ori')
print(f'7 apare de {k.count(7)} ori')
print(f'8 apare de {k.count(8)} ori')
print(f'9 apare de {k.count(9)} ori')
