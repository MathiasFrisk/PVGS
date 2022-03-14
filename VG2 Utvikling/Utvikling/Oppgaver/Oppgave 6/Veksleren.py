# Først lag en variabel der bruker kan sette inn pris på varene (kjopesum)
kjopesum = int(input("Hvor mye koster varen?: "))
# Lag en variabel der kjøper kan oppgi hvor mye de betaler med (belopsum)
belopsum = int(input("Hva betaler du med?: "))
# Lag en variabel der den skal regne ut hvor mye betaler skal få tilbake med belopsum - kjopesum
# Lag en print kommando som skriver ut hvor mange penger betaleren skal få tilbake 
tilbakepenger = belopsum - kjopesum
print(f"Penger du får tilbake er: {tilbakepenger},")
# lag en if setning som regner ut hvor mange ulike lapper og mynter skal få tilbake.

# En if-setning som kjører når veksletpenger er mer enn 500kr
if tilbakepenger >= 1000:
    print("Antall 1000-lapp: ",tilbakepenger // 1000)
    tilbakepenger = tilbakepenger % 1000
# En if-setning som kjører når veksletpenger er mer enn 500kr
if tilbakepenger >= 500:
    print("Antall 500-lapp: ",tilbakepenger // 500)
    tilbakepenger = tilbakepenger % 500
# En if-setning som kjører når veksletpenger er mer enn 200kr
if tilbakepenger >= 200:
    print("Antall 200-lapp: ",tilbakepenger // 200)
    tilbakepenger = tilbakepenger % 200
# En if-setning som kjører når veksletpenger er mer enn 100kr
if tilbakepenger >= 100:
    print("Antall 100-lapp: ",tilbakepenger // 100)
    tilbakepenger = tilbakepenger % 100
# En if-setning som kjører når veksletpenger er mer enn 50kr
if tilbakepenger >= 50:
    print("Antall 50-krone-lapp: ",tilbakepenger // 50)
    tilbakepenger = tilbakepenger % 50
# En if-setning som kjører når veksletpenger er mer enn 10kr
if tilbakepenger >= 10:
    print("Antall 10-krone: ",tilbakepenger // 10)
    tilbakepenger = tilbakepenger % 10
# En if-setning som kjører når veksletpenger er mer enn 5kr
if tilbakepenger >= 5:
    print("Antall 5-krone: ",tilbakepenger // 5)
    tilbakepenger = tilbakepenger % 5
# En if-setning som kjører når veksletpenger er mer enn 1kr
if tilbakepenger >= 1:
    print("Antall 1-krone: ",tilbakepenger // 1)
    tilbakepenger = tilbakepenger % 1