# import random
import random
# lag en variabel som heter antallforsok med verdien 0
# lag en variabel som heter skrivtall med verdien random.randrange
antallforsok = 0
tilfeldigtall = random.randrange(1,11)
# skriv til skjerm at du har startet tippe spill.
print("------------Du har startet tippe spill------------\n")
# Lag en variabel hvor spilleren kan skrive et tall
skrivtall = int(input("Skriv et tall mellom 1 til 10: "))
# Lag en if-setning som skal regne om tallet spilleren skrev er riktig/for høyt eller for lavt.
while skrivtall!=tilfeldigtall: 
    if skrivtall > tilfeldigtall:
        print("Tallet er for høyt\n")
    elif tilfeldigtall > skrivtall:
        print("Tallet er for lavt\n")
    skrivtall = int(input("Skriv et tall mellom 1 til 10: "))
    antallforsok += 1    
# skriv til skjerm hvor mange ganger før h*n fikk riktig.
else:
    print("tallet er riktig")
    print("Du brukte",antallforsok, "ganger for å klare det")   