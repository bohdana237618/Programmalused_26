from random import * #randint
from math import *
#Ülesanne1
print("Tere maailm")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try: 
    vanus=int(input("Sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks.")

     #Ülesanne 2
vanus=18 #int-täisarv
eesnimi="Jaak" #str-sõne
pikkus=16.5 
kas_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}") 

#Ülesanne 3
kommide_arv=randint(1, 100)        #int(input("Kommide arv: ")) 
print(f"Laud on {kommide_arv} kommi. ")
try:
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -=kommid 
    print(f"Laud on nüüd {kommide_arv} kommi.")
except ValueError:
    print("Palun sisesta number.")

#Ülesanne 4
try:
    ümbermõõt=float(input("Sisesta puu ümbermõõt: "))
    läbimõõt=round(ümbermõõt/pi,1)
    print(f"Puu läbimõõt on {läbimõõt}.")
except ValueError:
    print("Palun sisesta number.")

#Ülesanne 5
try:
    N=float(input("Sisesta ristküliku esimene külg (N): "))
    M=float(input("Sisesta ristküliku teine külg (M): "))

    diagonaal=round(sqrt(N**2 + M**2), 1)
    print(f"Ristküliku diagonaal on {diagonaal}.")
except ValueError:
    print("Palun sisesta kehtiv number.")

#Ülesanne 7
arv1=randint(1, 100)
arv2=randint(1, 100)
arv3=randint(1, 100)
arv4=randint(1, 100)
arv5=randint(1, 100)
summa=arv1+arv2+arv3+arv4+arv5
keskmine=summa/5
print(f"Summa: {summa}, Keskmine: {keskmine}")
try:
    jagaja=int(input("Sisesta arv, millega jagada: "))
    tulemus=summa/jagaja
    print("Tulemus:", tulemus) #tulemus=3.75
    print("Täisarvuline osa:", int(tulemus))
    #int(3.75)=3 teine variant täisosa leidmiseks on kasutada // jagam
    print("Jääk:", summa % jagaja)
except ValueError:
    print("Palun sisesta kehtiv number.")


