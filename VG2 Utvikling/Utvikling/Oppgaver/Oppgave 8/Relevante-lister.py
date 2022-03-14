# Lag først en variabel som heter "gangetabell" med input felt der bruker kan skrive hvilken gangetabell
gangetabell = int(input("Oppgi hvilken gangetabell: "))
# Lag en variabel med veriden null som heter "teller"
teller = 0
# lag en liste som heter "gange" som er tom
gange = []
# lag en while loop som at 10 er høyere en teller
    # teller er + 1 for at den skal ikke starte på null og ganger med hva bruker har tatt inn
while teller < 10:
    
    gange.append((teller+1)*gangetabell)
    teller = teller +1
	
# skriv til skjerm gange
print(gange)