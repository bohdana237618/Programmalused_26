print("Vali programm: ")
print("1-Arv kontroll")
print("2-Kehamissindeks")
print("3- Ostu allahindlus")
valik=input("Sisesta valik (1-3) => ")
if valik == "1":
#Arvu kontroll
#Ma parandasin: sõne alguses ja lõpus olid erinevad jutumärgid: 'Arvu kontroll"
    print("Arvu kontroll") 
    try:
        #Ma parandasin: input() tagastab teksti => Lisatud int()
        arv=int(input("Sisesta täisarv => "))
        #Ma parandasin: if arv>0 => puudus koolon
        if arv > 0:
            print("Arv on positiivne")
            #Ma parandasin: else if arv=0: peab olema elif arv==0
        elif arv == 0: 
            print("Arv on null")#Lisa 1: menüü, kus kasutaja valib, millist osa käivitada

        else:
            print("Arv on negatiivne")
        if arv % 2 == 0:
            #Ma parandasin:  taandrida-paarisarvu kontroll oli vales kohas (else sees) 
            print("Arv on paarisarv")
        else:
            print("Arv on paaritu")
            

#Lisa 2: kontroll, kas arv jagub 3-ga
        if arv % 3 == 0:
            print("Arv jagub 3-ga")
        else:
            print("Arv ei jagu 3-ga")
    except ValueError:
        print("Viga: sisesta täisarv")
elif valik == "2":
    #Kehamaasiindeks
    print("Kehamassindeks")
    try:
        #Ma parandasin: input() tagastab teksti => lisatud float()
        mass=float(input("Sisesta kaal (kg) => "))
        pikkus=float(input("Sisesta pikkus (m) => "))
        #Lisa 3: null ja negatiivsed väärtused pole lubatud
        if mass <= 0 or pikkus <=0:
            print("Viga: kaal ja pikkus peavad olema positiivsed")
        else:
            #Parandus: kmi=mass/pikkus*2=> peab olema pikkus**2
            kmi=mass/pikkus**2
            print("KMI:", round(kmi, 1))
            #Parandus: KMI tingimused olid valed
            #(Normaalkaal <25, Ülekaal < 30, Rasvumine >= 30)
            if kmi < 18.5:
                print("Alakaal")
            elif kmi < 25:
                print("Normaalkaal")
            elif kmi < 30:
                print("Ülekaal")
            else: 
                print("Rasvumine")
    except ValueError:
        print("Viga: sisesta arv")
elif valik == "3":
    #Ostu allahindlus
    print("Ostu allahindlus")
    try:
        #Parandus: input() tagastab teksti => lisatud float()
        summa=float(input("Sisesta ostusumma => "))
        if summa <= 0:
            #Parandus: summa=<0 => summa <=0
            print("Vigane summa")
        elif summa > 500:
            print("Allahindlus 10%, maksta:", round(summa*0.9, 2))
            #Parandus: summa>100 or summa<=500 => peab olema and (100 < summa <= 500)
        elif summa > 100: 
            print("Allahindlus 5%, maksta:", round(summa * 0.95, 2))
            #parandus: else: puudus koolon
        else:
            print("Allahindlust pole, maksta:", summa)
    except ValueError:
        print("Viga: sisesta arv")
else:
    print("Vigane valik") 



print("Vali programm:")
print("1 - Ruutvõrrandi lahendamine")
print("2 - Palga arvutamine")
print("3 - Parkimise hind")

valik = input("Sisesta valik (1-3) => ")

if valik == "1":
    # ---------- Ruutvõrrandi lahendamine ----------
    # Parandus: sõne alguses ja lõpus olid erinevad jutumärgid: "...'
    print("Ruutvõrrandi lahendamine")
    try:
        a = float(input("Sisesta a => "))
        b = float(input("Sisesta b => "))
        # Parandus: input() tagastab teksti -> lisatud float()
        c = float(input("Sisesta c => "))

        # Lisa: kui a on 0, siis see pole ruutvõrrand (nulliga jagamine)
        if a == 0:
            print("Viga: a ei tohi olla 0")
        else:
            D = b * b - 4 * a * c

            # Parandus: if D>0 -> puudus koolon
            if D > 0:
                # Parandus: /2*a -> peab olema /(2*a)
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                print("Kaks lahendit:", x1, x2)
            # Parandus: else if D=0: -> peab olema elif D==0:
            elif D == 0:
                x = -b / (2 * a)
                print("Üks lahend:", x)
            else:
                # Parandus: taandrida - print oli else-ga samal tasemel
                print("Reaalarvulised lahendid puuduvad")
    except ValueError:
        print("Viga: sisesta arv")

elif valik == "2":
    # ---------- Palga arvutamine ----------
    print("Palga arvutamine")
    try:
        tunnid = float(input("Sisesta töötunnid nädalas => "))
        tunnitasu = float(input("Sisesta tunnitasu (€) => "))

        # Parandus: tunnid<0 and tunnid>168 -> peab olema or
        # (arv ei saa olla korraga alla 0 ja üle 168)
        if tunnid < 0 or tunnid > 168:
            print("Vigane tundide arv")
        elif tunnid <= 40:
            palk = tunnid * tunnitasu
            print("Nädalapalk:", palk, "€")
        else:
            # Parandus: 1,5 -> peab olema 1.5 (punkt, mitte koma)
            palk = 40 * tunnitasu + (tunnid - 40) * tunnitasu * 1.5
            print("Nädalapalk koos ületundidega:", palk, "€")
    except ValueError:
        print("Viga: sisesta arv")

elif valik == "3":
    # ---------- Parkimise hind ----------
    print("Parkimise hind")
    try:
        tunnid = int(input("Sisesta parkimise aeg tundides => "))

        # Parandus: tunnid=<0 -> tunnid<=0
        if tunnid <= 0:
            print("Vigane aeg")
        # Parandus: tingimuste järjekord - kõigepealt >=8, siis >=3,
        # muidu 10 € haru ei täitunud kunagi
        elif tunnid >= 8:
            print("Hind: 10 € (päevapilet)")
        elif tunnid >= 3:
            print("Hind: 5 €")
        # Parandus: else: puudus koolon
        else:
            # Parandus: print lõpus puudus sulg )
            print("Hind: 2 €")
    except ValueError:
        print("Viga: sisesta täisarv")

else:
    print("Vigane valik")


 
