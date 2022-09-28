a1=float(input('primul numar:'))
a2=float(input('al doilea numar:'))
a3=float(input('al treilea numar:'))
a4=float(input('al parulea numar:'))
a5=float(input('al cincilea numar:'))
a6=float(input('al saselea numar:'))
a7=float(input('al saptelea numar:'))
a8=float(input('al optelea numar:'))
a9=float(input('al noulea numar:'))
a10=float(input('al zecilea numar:'))
def max(a,b):
    i=0
    if a>b:
        i=a
    elif b>a:
        i=b
    else:
        i=a
    return i
def min(a,b):
    i=0
    if a>b:
        i=b
    elif b>a:
        i=a
    else:
        i=a
    return i
print('S=','max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8))=',max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8)))
print('T=','min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)+max(a1,a2)+max(a3,a4)+max(a5,a6)+max(a7,a8)+max(a9,a10)=',min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)+max(a1,a2)+max(a3,a4)+max(a5,a6)+max(a7,a8)+max(a9,a10))