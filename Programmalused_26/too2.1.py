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
