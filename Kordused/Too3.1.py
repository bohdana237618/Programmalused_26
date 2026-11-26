while True:
    print("\nVali ülesanne:")
    print("1. Täisarvude loendamine")
    print("2. Naturaalarvude summa")
    print("3. Positiivsete arvude korrutis")
    print("4. Arvude ruudud")
    print("5. Negatiivsete arvude summa")
    print("6. Negatiivsed, positiivsed, nullid")
    print("7. K-ga jaguvad arvud")
    print("8. Tollid ja sentimeetrid")
    print("9. Pank ja intress")
    print("10. Paaride suurem arv")
    valik = input("Sisesta ülesande number (1-10) või 'q' väljumiseks: ")

    if valik == "1":
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
        for i in range(10, 21):
            print(i, "ruut:", i ** 2)

    elif valik == "5":
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
        try:
            N = int(input("Sisesta N: "))
            neg = 0
            pos = 0
            null = 0
            for i in range(N):
                arv = float(input(f"{i + 1}. arv: "))
                if arv < 0:
                    neg += 1
                elif arv > 0:
                    pos += 1
                else
                    null += 1
            print("Negatiivseid:", pos)
            print("Positiivseid:", neg)
            print("Nulle:", null)
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "7":
        try:
            A = int(input("Sisesta A: "))
            B = int(input("Sisesta B: "))
            K = int(input("Sisesta K: "))
            for i in range(A, B):
                if i % K = 0:
                    print(i)
        except ValueError:
            print("Palun sisesta täisarv.")
        except ZeroDivisionError:
            print("K ei tohi olla 0.")

    elif valik == "8":
        for toll in range(1, 20):
            print(toll "tolli =", toll * 2.5, "cm")

    elif valik == "9":
        try:
            S = float(input("Sisesta summa S: "))
            N = float(input("Sisesta aastate arv N: "))
            for i in range(N):
                S *= 3
            print("Summa", N, "aasta pärast:", round(S, 2))
        except ValueError:
            print("Palun sisesta arv.")

    elif valik == "10":
        try:
            for i in range(10):
                a = float(input("Esimene arv: "))
                b = float(input("Teine arv: "))
                if a > b:
                    print("Suurem:", a)
            else:
                    print("Suurem:", c)
        except ValueError:
            print("Palun sisesta arv.")

    elif valik.lower() == "q":
        print("Programmist väljumine...")
        break

    else:
        print("Viga: sisesta number 1-10 või 'q' väljumiseks.")