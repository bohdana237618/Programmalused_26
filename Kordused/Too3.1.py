while True:
    print("""
        1. Täisarvude loendamine
        2. Naturaalarvude summa
        3. Positiivsete arvude korrutis
        4. Arvude ruudud
        5. Negatiivsete arvude summa
        6.Klaviatuurilt sisestatakse N arvu.
          Koosta programm, mis määrab sisestatud arvude seast:
          negatiivsete arvude arvu,
          positiivsete arvude arvu,
          nullide arvu.(N väärtus sisestatakse klaviatuurilt.)
        7. Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].""")
    valik=input("Sisesta ülesande number (1-7) või 'q' väljumiseks: ")
    if valik == '1':
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
    elif valik == '2':
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
    elif valik == '3':
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
    elif valik == '4':
        for i in range(10, 21):
            print(i, "ruut:", i ** 2)
    elif valik == '5':
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
    elif valik == '6':
        while True:
            try:
                N = int(input("Sisesta arv N > 0: "))
                if N > 0: break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
                continue
        for i in range(N):
            while True:
                try:
                    arv = float(input(f"{i + 1}. arv: "))
                    break
                except ValueError:
                    print("Palun sisesta kehtiv arv.")
            if arv < 0:
                print("Negatiivne arv")
            elif arv > 0:
                print("Positiivne arv")
            else:
                print("Null")
    elif valik == '7':
        while True:
            try:
                A = int(input("Sisesta arv A: "))
                B = int(input("Sisesta arv B: "))
                K = int(input("Sisesta arv K: "))#Tee K kontroll, et see ei oleks 0
                if K == 0:
                    print("K ei tohi olla 0.")
                    continue
                break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
        if A > B:
            print("A peab olema väiksem või võrdne B-ga. Siis vahetame need.")
            A, B = B, A
        print(f"Arvud vahemikus [{A}, {B}], mis on {K}-ga jaguvad:")
        for i in range(A, B + 1):
            if i % K == 0:
                print(i)
    elif valik.lower() == 'q':
        print("Programmist väljumine...")
        break
    else:
        print("Viga: Palun sisesta number 1-7 või 'q' väljumiseks.")