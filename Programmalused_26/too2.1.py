eesnimi=input("Sisesta eesnimi: ")
if eesnimi.upper()=="JUKU": 
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju,Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")

#Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
try:
    vanus=int(input("Kui vana sa oled, Juku? "))
    if 0 <=vanus < 6:
        pilet="tasutapilet"
    elif 6 <= vanus <= 14:
        pilet="lastepilet"
    elif 14 < vanus < 65:
        pilet="täispilet"
    elif 65 <=vanus<= 100:
        pilet ="sooduspilet"
    else:
        print("Viga andmetes.")
    try:
        print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
    except NameError:
        print("Piletit ei saa määrata, kuna vanus on vale.")
except ValueError:
        print("Palun sisesta oma vanus numbrina. ")
else:
    print("Täna kinno ei minda.")
    #ülesanne "pinginaabrid"
pinginaabrid=["Anna", "Vika"]
nimi1=input("Sisesta esimese inimese nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid. ")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
    print("Viga: nimed peavad koosnema ainult tähtedest. ")
#otsing nimede algustähted järgi
valik=input("Kas soovid otsida nimede algustähtede järgi? (jah/ei): ").lower()
otsing=False 
if valik=="jah":
    algustäht=input("Sisesta algustäht: ").capitalize
    for nimi in pinginaabrid:
        if nimi.startswith(algustäht):
            print(f"{nimi} algab tähega {algustäht}. ")
            otsing=True
    if not otsing:
        print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud.")
else:
    print("Otsingut ei tehta. ")

#3. remont 
try:
    pikkus=float(input("Sisesta toa pikkus (m): "))
    laius=float(input("Sisesta toa laius (m): "))
    pindala=pikkus*laius
    print(f"Põranda pindala on {pindala} ruutmeetrit.")
    valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
    if valik=="jah":
        hind=float(input("Sisesta ruutmeetri hind (€): "))
        hind_kokku=pindala*hind
        print(f"Põranda vahetamise hind on {round(hind_kokku, 2)} eurot.")
        #lisaküsimus
        kes=input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
        if kes=="professionaal":
            too_hind=float(input("Sisesta töö hind ruutmeetri kohta (€): "))
            too_kokku=pindala*too_hind
            kogu_hind=hind_kokku+too_kokku
            print(f"Töö hind on {round(too_kokku, 2)} eurot.")
            print(f"Remondi koguhind koos tööga on {round(kogu_hind, 2)} eurot.")
        elif kes=="ise":
            print(f"Teed remondi ise, seega koguhind on {round(hind_kokku, 2)} eurot.")
