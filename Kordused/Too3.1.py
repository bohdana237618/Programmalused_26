import random

while True:
    print("\nVali ülesanne:")
    print("1. Täisarvude loendamine")
    print("2. Naturaalarvude summa")
    print("3. Positiivsete arvude korrutis")
    print("4. Arvude ruudud")
    print("5. Negatiivsete arvude summa")
    print("6. K-ga jaguvad arvud [A, B]")
    print("7. Tollid ja sentimeetrid")
    print("8. Pank ja intress")
    print("9. Paaride suurem arv")
    print("10. Niidukid")
    print("11. Faktoriaal")
    print("12. Diagonaal")
    print("13. Korrutustabel")
    print("14. Punktid ringis")
    print("15. Õpilaste keskmine pikkus")
    print("16. Mini-loterii")
    print("17. Spongi Bob ja kotletid")
    valik = input("Sisesta ülesande number (1-17) või 'q' väljumiseks: ")

    if valik == "1":
        # 1. 15 arvu, mitu täisarvu
        try:
            i = 0
            kogus = 0
            while i < 15:
                arv = float(input(f"{i + 1}. arv: "))
                if arv.is_integer():
                    kogus += 1
                i += 1
            print("Täisarve:", kogus)
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "2":
        # 2. Summa 1 kuni A
        try:
            while True:
                A = int(input("Sisesta arv A: "))
                if A > 0:
                    summa = 0
                    for i in range(1, A + 1):
                        summa += i
                    print("Summa:", summa)
                    break
                else:
                    print("Palun sisesta positiivne täisarv.")
        except ValueError:
            print("Palun sisesta kehtiv täisarv.")

    elif valik == "3":
        # 3. 8 arvu, positiivsete korrutis
        try:
            korrutis = 1
            i = 0
            while True:
                arv = float(input(f"{i + 1}. arv: "))
                if arv > 0:
                    korrutis *= arv
                i += 1
                if i == 8:
                    break
            print("Korrutis:", korrutis)
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "4":
        # 4. Ruudud 10 kuni 20
        for i in range(10, 21):
            print(i, "ruut:", i ** 2)

    elif valik == "5":
        # 5. Negatiivsete arvude summa
        try:
            while True:
                N = int(input("Sisesta arv N > 0: "))
                if N > 0:
                    break
            summa = 0
            for i in range(N):
                arv = float(input(f"{i + 1}. arv: "))
                if arv < 0:
                    summa += arv
            print("Negatiivsete arvude summa:", summa)
        except ValueError:
            print("Palun sisesta täisarv.")

    elif valik == "6":
        # 6. K-ga jaguvad arvud vahemikus [A, B]
        try:
            A = int(input("Sisesta A: "))
            B = int(input("Sisesta B: "))
            K = int(input("Sisesta K: "))
            if K == 0:
                print("K ei tohi olla 0.")
            else:
                for i in range(A, B + 1):
                    if i % K == 0:
                        print(i, end=" ")
                print()
        except ValueError:
            print("Palun sisesta täisarv.")

    elif valik == "7":
        # 7. Tollid ja sentimeetrid
        for toll in range(1, 21):
            print(toll, "tolli =", toll * 2.5, "cm")

    elif valik == "8":
        # 8. Pank, 3% intress
        try:
            S = float(input("Sisesta summa S: "))
            N = int(input("Sisesta aastate arv N: "))
            for i in range(N):
                S *= 1.03
            print("Summa", N, "aasta pärast:", round(S, 2), "eurot")
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "9":
        # 9. 10 arvu paari, väljasta suurem
        try:
            for i in range(10):
                a = float(input(f"{i + 1}. paar, esimene arv: "))
                b = float(input(f"{i + 1}. paar, teine arv: "))
                if a > b:
                    print("Suurem:", a)
                elif b > a:
                    print("Suurem:", b)
                else:
                    print("Arvud on võrdsed:", a)
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "10":
        # 10. Niidukid
        try:
            N = int(input("Sisesta niidukite arv N: "))
            m = float(input("Sisesta, mitu tundi töötas esimene niiduk (m): "))
            kokku = 0
            for i in range(N):
                kokku += m + i * 10 / 60
            print("Brigaad töötas kokku", round(kokku, 2), "tundi")
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "11":
        # 11. Korrutis 1 kuni N (N juhuslik)
        N = random.randint(1, 10)
        korrutis = 1
        for i in range(1, N + 1):
            korrutis *= i
        print("N =", N)
        print("Korrutis 1 kuni N:", korrutis)

    elif valik == "12":
        # 12. Diagonaal
        for i in range(1, 10):
            for j in range(1, 10):
                if i == j:
                    print(i, end=" ")
                else:
                    print(0, end=" ")
            print()

    elif valik == "13":
        # 13. Korrutustabel
        try:
            arv = int(input("Sisesta arv: "))
            for i in range(1, 10):
                print(f"{arv}*{i}={arv * i}")
        except ValueError:
            print("Palun sisesta täisarv.")

    elif valik == "14":
        # 14. Punktid ringis
        try:
            N = int(input("Sisesta punktide arv N: "))
            R = float(input("Sisesta raadius R: "))
            a = float(input("Sisesta keskpunkti a: "))
            b = float(input("Sisesta keskpunkti b: "))
            loendur = 0
            for i in range(N):
                x = float(input(f"{i + 1}. punkti x: "))
                y = float(input(f"{i + 1}. punkti y: "))
                if (x - a) ** 2 + (y - b) ** 2 < R ** 2:
                    loendur += 1
            print("Ringi sees on", loendur, "punkti")
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "15":
        # 15. Õpilaste keskmine pikkus
        try:
            while True:
                N = int(input("Sisesta õpilaste arv N > 0: "))
                if N > 0:
                    break
            summa = 0
            for i in range(N):
                pikkus = float(input(f"{i + 1}. õpilase pikkus (cm): "))
                summa += pikkus
            print("Keskmine pikkus:", round(summa / N, 2), "cm")
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "16":
        # 16. Mini-loterii
        salajane = random.randint(1, 100)
        katseid = 0
        print("Arvasin ära arvu vahemikus 1-100. Arva ära!")
        while True:
            try:
                arv = int(input("Sinu pakkumine: "))
            except ValueError:
                print("Palun sisesta täisarv.")
                continue
            katseid += 1
            if arv < salajane:
                print("Liiga väike!")
            elif arv > salajane:
                print("Liiga suur!")
            else:
                print("Õige! Katseid:", katseid)
                break

    elif valik == "17":
        # 17. Spongi Bob ja kotletid
        try:
            K = int(input("Mitu kotletti (K): "))
            M = int(input("Mitu kotletti mahub pannile (M): "))
            if M <= 0:
                print("M peab olema positiivne.")
            else:
                print("Täis pannitäisi:", K // M)
                print("Kotlette jääb viimasele pannile:", K % M)
        except ValueError:
            print("Palun sisesta täisarv.")

    elif valik.lower() == "q":
        print("Programmist väljumine...")
        break

    else:
        print("Viga: sisesta number 1-17 või 'q' väljumiseks.")