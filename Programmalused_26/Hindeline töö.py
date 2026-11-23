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


 
