import math
print("Hello, \nWorld!")
print("Tere tulemast\t!")
print("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik


#Parametrid sep ja end
print() #see on tühi rida
print("Õpin",1,".kursusel",sep="***") #sep="" tähendab,et tühikut ei ole
print("2026", "10", "01", sep="/")
print("Sama ", end="") #end="" tähendab, et reavahetuset eo ole end="\n"
print("rida")


#Muutujad
nimi = "Python" #str ehk sõne
print("Tere,", nimi)
Kursus=1
print("Õpin",Kursus,".kursusel")

# inpot() funktsioon
nimi = input("Sisesta oma nimi: ") #programm küsib ja ootab kasutaja sisestust
print("Tere,", nimi)
Kursus=int(input("Sisesta kursuse number: ")) #teiesendab sõne arvuks
print("Õpin",Kursus,".kursusel")
print("Järgmisel aasta õpin ",Kursus+1,".Kursusel") 
#Kursus+1 tähendab, et kursuse number suureneb 1 võrra")

print("Liitmine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"+",b,"=",a + b) 

print("Lahutamine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"-",b,"=",a - b)

print("Korrutamine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"*",b,"=",a * b)

print("Jagamine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"/",b,"=",round(a / b,2))

print("Asendamine")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"**",b,"=",a ** b)

print("Jagamise täisarvuline osa")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"//",b,"=",a // b)

print("Jagamisjääk")
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"%",b,"=",a % b)

#f-sõne formatimine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a =float(input("Esimene arv"))
tehe=input("Tehe: ")
b =float(input("Teine arv: "))

print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")


print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))
