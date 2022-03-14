# Lag en print kommando som skal hilse på brukeren når programmet starter
print("------- Velkommen til Ekstraoppgave-03 - Trille terning -------")
# Bruk import funksjon for å hente random module fra python bibliotek
import random

# Lag en variabel som skal telle opp antall kast brukeren trenger for å få en sekser med tallet 1 som start verdi
antallkast = 1

# Lag en while løkke for å gjenta kode inntil at brukeren får en sekser
while antallkast:

# Lag en variabel som inneholder en randint funksjon som tar et tilfeldig tall fra 1 til 6 inne while løkkeren
    randomtall = random.randint(1, 6)

# Skriv ut til skjerm antall runder i sanntid
    print(antallkast, "runde. ",randomtall)

# Antallkast økes med en hvergang terning ikke er en 6
    antallkast += 1
# en if setning som kjøres når terning er 6
    if randomtall == 6:
        print("Wooooooow")
# Skriv ut til skjerm antall runde det tok før brukeren fikk 6
        print(f"Det tok {antallkast} kast for å kunne få 2 seksere")
# Break for å stoppe while løkkeren
        break