import math


def get_leap_years(start: int, end: int):
    list = []
    for i in range(start, end + 1):
        if i % 4 == 0 and i % 100 != 0:
            list.append(i)
        elif i % 400 == 0:
            list.append(i)
    return list


def test_get_leap_years():
    assert get_leap_years(2000, 2022) == [2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(1990, 2000) == [1992, 1996, 2000]
    assert get_leap_years(1980, 1990) == [1980, 1984, 1988]


def get_perfect_squares(start: int, end: int):
    list = []
    for i in range(start, end + 1):
        if int(math.sqrt(i)) == float(math.sqrt(i)):
            list.append(i)
    return list


def test_get_perfect_squares():
    assert get_perfect_squares(10, 50) == [16, 25, 36, 49]
    assert get_perfect_squares(60, 80) == [64]
    assert get_perfect_squares(80, 100) == [81, 100]


def is_palindrome(n):
    inv = 0  # inversul lui n
    x = n  # copie a lui n
    while n:
        inv = inv * 10 + n % 10
        n //= 10
    return inv == x  # returneaza 1 daca n e palindrom sau 0 in caz contrar


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12) == False
    assert is_palindrome(11) == True


test_get_leap_years()
test_get_perfect_squares()
test_is_palindrome()


def main():
    shouldRun = True
    while shouldRun == True:
        problema = input("Da numarul problemei: ")
        if problema == "1":
            print("Rezolvi problema 1: afiseaza toti anii bisecti intre doi ani dati(inclusiv anii dati) ")
            x = int(input("Alege inceputul intervalului: "))
            y = int(input("Alege utimul element al intervalului: "))
            listaAni = get_leap_years(x, y)
            print("Anii bisecti din intervalul dat sunt: " + ", ".join(str(an) for an in listaAni))
        elif problema == "2":
            print("Rezolvi problema 2: afiseaza toate patratele perfecte dintr-un interval inchis dat")
            x = int(input("Alege inceputul intervalului: "))
            y = int(input("Alege utimul element al intervalului: "))
            listaPatratePerfecte = get_perfect_squares(x, y)
            print("Patratele perfecte  din intervalul dat sunt: " + ",".join(str(an) for an in listaPatratePerfecte))
        elif problema == "3":
            print("Rezolvi problema 3: Determina daca un numar dat este palindrom")
            x = int(input("Citeste n: "))
            rezultat = is_palindrome(x)
            if rezultat == True:
                print("Numarul ales este palindrom")
            else:
                print("Numarul ales nu este palindrom")
        elif problema == "x":
            print("Ai inchis programul")
            shouldRun = False
        else:
            print("Ai ales un numar gresit, te rog alege din nou! ")

    pass


if __name__ == "_main_":
    main()