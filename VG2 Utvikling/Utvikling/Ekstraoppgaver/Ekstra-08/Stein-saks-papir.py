# hent inn random funksjon fra python biblioteket
import random
# Lag en variabel som teller runder spilt med start verdien 0
tapp = 0
vinn = 0
# Lag en liste som inneholder stein saks papir
spill_liste = ["stein", "saks", "papir"]
# skriv til skjerm at spillet har startet
print("-------- Du har startet Stein saks papir! --------")
# Lag et inputfelt hvor brukeren kan skrive inn stein, saks eller papir

# Lag en while løkke som gjentar programmet
while vinn < 3:
    programsvar = random.choice(spill_liste)
    brukersvar = input("Stein, saks eller papir?: ")
    # Masse if setninger
    if brukersvar == "papir" and programsvar == "stein":

        print("you win")
        vinn += 1
    
    if brukersvar == "saks" and programsvar == "papir":
        print("Porgrammet valgte",programsvar)
        print("you win")
        vinn += 1

    if brukersvar == "stein" and programsvar == "saks":
        print("Porgrammet valgte",programsvar)
        print("you win")
        vinn += 1

    if brukersvar == "saks" and programsvar == "stein":
        print("Porgrammet valgte",programsvar)
        tapp += 1
        print("you lose")
    
    if brukersvar == "papir" and programsvar == "saks":
        print("Porgrammet valgte",programsvar)
        tapp += 1
        print("you lose")

    if brukersvar == "stein" and programsvar == "papir":
        print("Porgrammet valgte",programsvar)
        tapp += 1
        print("you lose")
    
    if brukersvar == programsvar:
        print("Porgrammet valgte",programsvar)
        print("Draw!")

    if tapp == 3:
        break   
# skriv til skjerm om brukeren vant eller tapte
