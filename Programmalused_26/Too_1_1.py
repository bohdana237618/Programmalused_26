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

      # Ülesanne 1

from datetime import *

täna = date.today()
print(f"Täna on {täna}")

print(täna.strftime("%d/%m/%Y"))
print(täna.strftime("%B %d, %Y"))
print(täna.strftime("%m/%d/%y"))
print(täna.strftime("%b-%d-%Y"))


# Ülesanne 2

print(3 + 8 / (4 - 2) * 4)
print(3 + 8 / 4 - 2 * 4)
print((3 + 8) / (4 - 2) * 4)


# Ülesanne 3

from math import *

R = float(input("Sisesta ringi raadius: "))

ruudu_pindala = (2 * R) ** 2
ruudu_umbermoot = 8 * R

ringi_pindala = pi * R ** 2
ringi_umbermoot = 2 * pi * R

print("Ruudu pindala:", ruudu_pindala)
print("Ruudu ümbermõõt:", ruudu_umbermoot)
print("Ringi pindala:", ringi_pindala)
print("Ringi ümbermõõt:", ringi_umbermoot)


# Ülesanne 4

from math import *

maa_raadius = 6378
mundi_labimoot = 0.02575

maa_umbermoot = 2 * pi * maa_raadius
muntide_arv = maa_umbermoot / (mundi_labimoot / 1000)

print("Maa ümbermõõt:", maa_umbermoot, "km")
print("Müntide arv:", round(muntide_arv))


# Ülesanne 5

sona = "kill-koll"

print((sona + " ") * 2 + "killadi-koll", end=" ")
print((sona + " ") * 2 + "killadi-koll", end=" ")
print((sona + " ") * 3)
print(sona)


# Ülesanne 6

laul = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""

print(laul.upper())


# Ülesanne 7
try: 
    a = float(input("Sisesta esimene külg: "))
    b = float(input("Sisesta teine külg: "))

    umbermoot = 2 * (a + b)
    pindala = a * b

    print("Ümbermõõt:", umbermoot)
    print("Pindala:", pindala)
except ValueError: 

# Ülesanne 8

liitrid = float(input("Sisesta kütuse liitrid: "))
kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

kulu = liitrid / kilomeetrid * 100

print("Kütusekulu 100 km kohta:", kulu)


# Ülesanne 9

kiirus = 29.9
minutid = float(input("Sisesta minutid: "))

kaugus = kiirus * minutid / 60

print("Läbitud kaugus:", kaugus, "km")


# Ülesanne 10

minutid = int(input("Sisesta minutid: "))

tunnid = minutid // 60
jaak = minutid % 60

print(f"{tunnid}:{jaak:02d}")  


