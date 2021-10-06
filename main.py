
def numarPrim(x):
    nr=0
    if x<2:
        return False
    for i in range (2,x//2+1):
        if x%i==0:
            nr=nr+1
    if nr==0:
        return True
    else:
        return False
def testNumarPrim():
    assert(numarPrim(3))==True
    assert(numarPrim(11))==True
    assert(numarPrim(4))==False
testNumarPrim()

def ultimulNrPrim(x):
    y=x-1
    k=0
    while k==0:
        if numarPrim(y)==True:
            k=1
        else:
            y=y-1
        return y

def testUltimulNrPrim():
    assert (ultimulNrPrim(7)==5)
    assert (ultimulNrPrim(20)==19)
    assert (ultimulNrPrim(43)==41)
testUltimulNrPrim()

def meniu():
    print("1.Afiseaza ultimul numar prim mai mic decat x")
    print("0. Iesire")

def interfata():
    meniu()
    x=int(input("Dati un numar x:"))
    while True:
        op=int(input("Optiunea este:"))
        if op==1:
            print("Ultimul nr prim mai mic decat x este:" "ultimulNrPrim(x)")
        elif op==0:
            break
        else:
            print ("invalid")
interfata()

def baza(n):

    m=0
    p=1
    while n>0:
        r=n%2
        m=m+r*p
        p=p*10
        n=n//2
    return m

def meniu():
    n=int(input("n="))

    print (n,"scris in baza 2 este:", baza(n))
meniu()
