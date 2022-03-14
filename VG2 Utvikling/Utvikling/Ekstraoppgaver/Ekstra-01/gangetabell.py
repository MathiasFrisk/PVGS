# Hent random funksjon fra biblioteket
import random
# Lag print kommandoer som skal hilse på brukeren og fortelle hva oppgaven handler om
print("---------- Velkommen til gangetabelløvelse! ----------")
print("Du skal nå få 10 tilfeldige multiplikasjonsstykker og du skal svare på de")
# Lag to variabeler som velger to tilfeldige tall mellom 1 og 10 med bruk av randint metoden
 
# En print kommando som viser de to tilfeldige tallene til skjerm
# Et inputfeltet som ber brukeren til å oppgi svaret på multiplikasjonen av disse to tallene.
# Lag en variabel som skal telle opp hvor mange rette svar brukeren fikk, gi en start verdi
poeng = 0
 
# Lag en for loop slik at brukeren skal få 10 multiplikasjonsstykker 
for quiz in range(10):
    tilfeldigtall1 = random.randint(1, 10)
    tilfeldigtall2 = random.randint(1, 10)      
    print(f"{tilfeldigtall1} * {tilfeldigtall2}")
    brukersvar = int(input("Oppgi svaret ditt: "))
    fasit = tilfeldigtall1 * tilfeldigtall2
    
    if brukersvar == fasit:
        print("Riktig!!")
        poeng += 1
    else: 
        print("Feil!")
 
    # Lag en if-setning som skal kjøre når brukeren får 10 rette svar
if poeng == 10:
    print("Supert! du er god!, poengsum: ", poeng) 
    # Lag en if-setning som skal kjøre når brukeren får 9 rette svar
elif poeng == 9:
    print("Dette var bra, poengsum: ", poeng) 
    # Lag en if-setning som skal kjøre når brukeren får 8 rette svar
elif poeng == 8:
    print("Bra, men du kan øve mer!, poengsum: ", poeng) 
    # Lag en if-setning som skal kjøre når brukeren får 7 rette svar
elif poeng <= 7:
    print("Du må øve mer, poengsum: ", poeng) 
