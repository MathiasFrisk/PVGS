"""
def tekst_til_skjerm(navn):
    for teller in range(10):
        print("Hei på deg", navn)


svar = input("Oppgi nvavnet ditt: ")
tekst_til_skjerm(svar)
"""

def areal_sirkel(radius):
    areal = 3,14*radius**2
    return areal

svar = float(input("oppgi en radius: "))
print(areal_sirkel(svar))
