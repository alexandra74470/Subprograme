
n=int(input("n="))
if n<=100000:
    """
    def nr_c(x):
        nr=0
        while(x>0):
            r=x%10
            x//=10
            nr=nr+1
        return nr
    print(f"Numarul de cifre este: {nr_c(n)}")
    """
    """
    Determinarea numarului  de cifre pare
    def nr_c(x):
        l=[]
        while x>0:
            l.append(x%10)
            x//=10
        par=[]
        for i in l:
            if i%2==0:
                par.append(i)
        return len(par)
print(f"Numarul de cifre pare este {nr_c(n)}")
    """
    """
    Determinarea numarului de cifre impare
    def nr_c(x):
        l=[]
        while x>0:
            l.append(x%10)
            x//=10
        impar=[]
        for i in l:
            if i%2==1:
                impar.append(i)
        return len(impar)
print(f"Numarul de cifre impare este {nr_c(n)}")
    """
    """
    def suma_cifrelor(x):
        s=0
        while(x>0):
            r=x%10
            x//=10
            s+=r
        return s
    print(f"Suma cifrelor este : {suma_cifrelor(n)}")
    """
    """
    def cifra_maxima(x):
        max=0
        while(x>0):
            r=x%10
            x//=10
            if r>max:
                max=r
        return max
print(f"Cifra maxima este {cifra_maxima(n)}")
    """
    """
    def cifra_minima(x):
        min=9
        while(x>0):
            r=x%10
            x//=10
            if r<min:
                min=r
        return min
print(f"Cifra minima este : {cifra_minima(n)}")
    """
    """
    def media_aritmetica(x):
        return suma_cifrelor(x)/nr_c(x)
    print(f"Media aritmetica de la x : {media_aritmetica(n)}")
    """
    """
    def repeta(x):
        lst=[]
        x=str(x)
        for i in x:
            if x.count(i)>=2:
                if i not in lst:
                    lst.append(i)
        return lst
    print(f"Cifre minim de 2 ori sunt {repeta(n)}")
    """
    def spatiu(x):
        y=""
        x=str(x)
        for i in x:
            if x==" ":
                y=x
if n>100000:
    print("Numarul trebuie sa fie in interval pana la 100000")