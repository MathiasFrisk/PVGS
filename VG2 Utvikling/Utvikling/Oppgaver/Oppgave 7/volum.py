# Lager en funksjon med navn volum_boks som skal hente verdien til inputen høyde
def volum_høyde(høyde):
    # lag en variabel som heter "Lengde" med verdien 29,7
    # lag en variabel som heter "Bredde" med verdien 21 
    lengde = 29.7
    bredde = 21
    # Lager en variabel med navn volum som skal regne ut volumet
    volum = høyde*(lengde-(høyde*2))*(bredde-(høyde*2))
    # Lager return som skal returnere volum
    return volum
    # Lager en input der brukeren kan skrive inn høyde
    # Lager til slutt print som skal skrive ut resultatet
print("Volumet blir: ", (volum_høyde(float(input("Skriv inn høyde: ")))))