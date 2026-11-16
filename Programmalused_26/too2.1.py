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

        kes=input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
        if kes=="professionaal":
            too_hind=float(input("Sisesta töö hind ruutmeetri kohta (€): "))
            too_kokku=pindala*too_hind
            kogu_hind=hind_kokku+too_kokku
            print(f"Töö hind on {round(too_kokku, 2)} eurot.")
            print(f"Remondi koguhind koos tööga on {round(kogu_hind, 2)} eurot.")
        elif kes=="ise":
            print(f"Teed remondi ise, seega koguhind on {round(hind_kokku, 2)} eurot.")
        else:
            print("Palun vali 'ise' või 'professionaal'.")
    else:
            print("Täna remonti ei tee.")
except ValueError:
    print("Viga: palun sisesta arv.")


#4. allahindlus
try:
    alghind=float(input("Sisesta toote alghind (€): "))
    if alghind>700:
        lopphind=alghind*0.7
        print(f"Hind on üle 700 eurot, seega soodustus 30%. Lõplik hind on {lopphind:.2f} eurot.")
    else:
        print(f"Soodustust ei ole. Lõplik hind on {alghind:.2f} eurot.")
except ValueError:
    print("Viga: palun sisesta arv.") 


    #5. temperatuur
try:
    temp=float(input("Sisesta toatemperatuur (°C): "))
    if temp>18:
        print("Temperatuur on üle 18 kraadi, see sobib talvel.")
    else:
        print("Temperatuur on 18 kraadi või alla selle, see on talvel liiga külm.")
except ValueError:
    print("Viga: palun sisesta temperatuur numbrina.")


    #6. pikkus
#lühike: alla 160 cm
#keskmine: 160-180 cm
#pikk: üle 180 cm
try:
    pikkus=float(input("Sisesta oma pikkus sentimeetrites: "))
    if pikkus<160:
        print("Sa oled lühike.")
    elif pikkus<=180:
        print("Sa oled keskmise pikkusega.")
    else:
        print("Sa oled pikk.")
except ValueError:
    print("Viga: palun sisesta pikkus numbrina. ")

#7. pikkus ja sugu
#mehed: lühike alla 170 cm, keskmine 170-185 cm, pikk üle 185 cm
#naised: lühike alla 160 cm, keskmine 160-175 cm, pikk üle 175 cm
try:
    pikkus=float(input("Sisesta oma pikkus sentimeetrites: "))
    sugu=input("Sisesta oma sugu (M/N): ").lower() 
    if sugu=="m" or sugu=="mees":
        if pikkus<170:
            print("Sa oled lühike.")
        elif pikkus<=185:
            print("Sa oled keskmise pikkusega.")
        else:
            print("Sa oled pikk.")
    elif sugu=="n" or sugu=="naine":
        if pikkus<160:
            print("Sa oled lühike.")
        elif pikkus<=175:
            print("Sa oled keskmise pikkusega.")
        else:
            print("Sa oled pikk.")
    else:
        print("Viga: sugu on sisestatud valesti.")
except ValueError:
    print("Viga: palun sisesta pikkus numbrina.")


#8. poes
from random import uniform

#ilma tsüklita ja listita
summa=0
arve="Toode   Kogus   Hind   Kokku"

#piim
valik=input("Kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju piima soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        piim_hind=round(uniform(0.5, 3), 2)
        print(f"Piima hind on {piim_hind} eurot.")
        summa+=kogus*piim_hind
        print(f"Piima kogusumma on {round(kogus*piim_hind, 2)} eurot.")
        arve+=f"\nPiim   {kogus}   {piim_hind}   {round(kogus*piim_hind, 2)}"
    else:
        print("Viga: kogus peab olema täisarv.")
else:
    print("Piima ei osta.")

#sai
valik=input("Kas soovid osta saia? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju saia soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        sai_hind=round(uniform(0.5, 3), 2)
        print(f"Saia hind on {sai_hind} eurot.")
        summa+=kogus*sai_hind
        print(f"Saia kogusumma on {round(kogus*sai_hind, 2)} eurot.")
        arve+=f"\nSai   {kogus}   {sai_hind}   {round(kogus*sai_hind, 2)}"
    else:
        print("Viga: kogus peab olema täisarv.")
else:
    print("Saia ei osta.")

    #leib
valik=input("Kas soovid osta leiba? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju leiba soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        leib_hind=round(uniform(0.5, 3), 2)
        print(f"Leiva hind on {leib_hind} eurot.")
        summa+=kogus*leib_hind
        print(f"Leiva kogusumma on {round(kogus*leib_hind, 2)} eurot.")
        arve+=f"\nLeib   {kogus}   {leib_hind}   {round(kogus*leib_hind, 2)}"
    else:
        print("Viga: kogus peab olema täisarv.")
else:
    print("Leiba ei osta.")

#munad
valik=input("Kas soovid osta mune? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju mune soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        munad_hind=round(uniform(0.5, 3), 2)
        print(f"Munade hind on {munad_hind} eurot.")
        summa+=kogus*munad_hind
        print(f"Munade kogusumma on {round(kogus*munad_hind, 2)} eurot.")
        arve+=f"\nMunad   {kogus}   {munad_hind}   {round(kogus*munad_hind, 2)}"
    else:
        print("Viga: kogus peab olema täisarv.")
else:
    print("Mune ei osta.")

#juust
valik=input("Kas soovid osta juustu? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju juustu soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        juust_hind=round(uniform(0.5, 3), 2)
        print(f"Juustu hind on {juust_hind} eurot.")
        summa+=kogus*juust_hind
        print(f"Juustu kogusumma on {round(kogus*juust_hind, 2)} eurot.")
        arve+=f"\nJuust   {kogus}   {juust_hind}   {round(kogus*juust_hind, 2)}"
    else:
        print("Viga: kogus peab olema täisarv.")
else:
    print("Juustu ei osta.")

#tšekk
print("\n----- TŠEKK -----")
print(arve)
print(f"Kogusumma: {round(summa, 2)} eurot.")

#9. ruut
try:
    a=float(input("Sisesta esimese külje pikkus: "))
    b=float(input("Sisesta teise külje pikkus: "))
    c=float(input("Sisesta kolmanda külje pikkus: "))
    d=float(input("Sisesta neljanda külje pikkus: "))
    if a>0 and b>0 and c>0 and d>0:
        if a==b and b==c and c==d:
            print("Tegemist on ruuduga.")
        else:
            print("Tegemist ei ole ruuduga.")
    else:
        print("Viga: kõik pikkused peavad olema positiivsed.")
except ValueError:
    print("Viga: palun sisesta pikkus numbrina.")

#10. matemaatika
try:
    arv1=float(input("Sisesta esimene arv: "))
    arv2=float(input("Sisesta teine arv: "))
    tehe=input("Vali tehe (+, -, *, /): ")
    if tehe=="+":
        print(f"Tulemus: {arv1} + {arv2} = {arv1+arv2}")
    elif tehe=="-":
        print(f"Tulemus: {arv1} - {arv2} = {arv1-arv2}")
    elif tehe=="*":
        print(f"Tulemus: {arv1} * {arv2} = {arv1*arv2}")
    elif tehe=="/":
        if arv2==0:
            print("Viga: nulliga ei saa jagada.")
        else:
            print(f"Tulemus: {arv1} / {arv2} = {arv1/arv2}")
    else:
        print("Viga: tundmatu tehtemärk.")
except ValueError:
    print("Viga: palun sisesta arv.")