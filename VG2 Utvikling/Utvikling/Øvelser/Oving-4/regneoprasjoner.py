# Lag to variabler for tall
tall1_txt = input("Oppgi tall nr 1 ")
tall2_txt = input("Oppgi tall nr 2 ")
valg = ("Hvilken regneart vil du bruke?:")
# Koverter text variabel til tall
tall1 = float(tall1_txt)
tall2 = float(tall2_txt)

# Addisjon
if valg == "+":
    print(tall1 , " + " , tall2 , " = " ,tall1 + tall2)