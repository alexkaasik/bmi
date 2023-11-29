print("Tere! Olen sinu uus sõber - Python!")
nimi= input("nimi: ")
print(f"{nimi}")

print(f"{nimi}, oi kui ilus nimi!")
answer = str(input(f"{nimi}! Kas leian Sinu keha indeksi? 1-jah või 0-ei?: "))
try:
    if answer.lower() == "jah" or answer.lower() == "1":
        pikkus=int(input("pikkus(cm): "))
        mass=float(input("mass(kg): "))
        indeks= mass/(0.01*pikkus)**2
        if indeks >= 40:
            index="Tervisele ohtlik rasvumine"
        elif 35 <= indeks <= 40:
            index="Tugev rasvumine"
        elif 30 <= indeks <= 35:
            index="Rasvumine"
        elif 25 <= indeks <= 30:
            index="Ülekaal"
        elif 19 <= indeks <= 25:
          index="Normaalkaal"
        elif 16 <= indeks <= 19:
            index="Alakaal"
        elif 0 <= indeks <= 16:
            index="Tervisele ohtlik rasvumine"
        else:
            index="Kahju! See on väga kasulik info!\n"

        print(f"{nimi}! Sinu keha indeks on:{round(indeks,1)} BMI - {index}")
        
    else:
        print("Kahju! See on väga kasulik info!\n")
except:
    pass

print(f"Kohtumiseni,{nimi}!Igavesti Sinu, Python!")