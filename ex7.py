from random import randint
v=[]
for i in range(10):
    for x in range(5):
        v.append(randint(1,36))
    print(v)
    v.clear()
