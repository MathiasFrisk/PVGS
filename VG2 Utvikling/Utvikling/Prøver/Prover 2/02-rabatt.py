# lag en variabel som inneholder en input felt der bruker kan skrive inn pris
gammelpris = (int(input("Hva er prisen som skal få en rabatt? ")))
# Lag en variabel med rabatten fks "10%"
prosentsats = 10
# Lag en funksjon som regner ut den nye prisen.
nypris=gammelpris -gammelpris*prosentsats/100
# Skriv til skjerm ny og gammel pris
print("-------- Gammel pris --------")
print(gammelpris,"kr")
print("-------- Ny pris --------")
print(nypris,"kr")