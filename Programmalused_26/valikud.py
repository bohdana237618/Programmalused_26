#Lihtne if
x = -5 #Testimiseks kirjuta siia mõni arv
try:
    x=int(input("Sisesta täisarv: "))
    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")
    print("See rida täidetakse alati")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

#if else
try:
    x = int(input("Sisesta arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except ValueError:
    print("Palun sisesta kehtiv täisarv. ")

vastus = input("Kas soovid jätkata? (jah/ei) ")
print("Sinu vastus oli:", vastus)
# vastuse_tüüp=type(vastus)
# print("Vastuse tüüp on: ", vastuse_tüüp)
# kas_vastus_on_tekst=vastus.isalpha()
# print("Kas see on tekst:",kas_vastus_on_tekst)
if vastus.isalpha():
    if vastus.lower() == "jah":
        print("Jätkame!")
    else:
        print("Head aega!") 
else: 
    print("Palun sisesta ´jah´ või ´ei´. ")

#if...elf...else
try: 
    x = int(input("Sisesta arv -5 kuni 5: "))
    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")
except:
    print("Sisesta kehtiv täisarv. ")

#if on if´i sees

nimi = input("Sisesta nimi: ")
print("Ainult tähed:", nimi.isalpha())
print("Suurtähtedega:", nimi.isupper())
print("Algab suurtähega:", nimi.istitle())
if nimi.isalpha() and nimi.istitle():
    print("Nimi sobib.")
    try:
        vanus = int(input("Vanus: "))
        if vanus >= 18:
            juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võid autot juhtida.")
            elif juhiluba.lower() == "ei": 
                print("Kõigepealt tee juhiload.")
            else: 
                print(f"Ära vasta {juhiluba}. Vasta jah või ei")
        else:
            print("Oled autojuhtimiseks liiga noor.")
    except: 
            print("Palun sisesta kehtiv arv. ")
    else:
        print("Nimes tohib olla ainult tähti!")



