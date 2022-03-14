#   Opprett grønn kopp
#   Gir grønn kopp verdien *rød penn*
grønnkopp = "rødpenn"
#   Opprett sort kopp
#   Gir sort kopp verdien *blå penn*  
sortkopp = "blåpenn"
#   Opprett hvit kopp
#   Gir hvit kopp verdien *null*

#   Skriv innholdet til grønnkopp til skjerm
print("Grønnkopp", grønnkopp)
#   Skriv innholdet til sortkopp til skjerm 
print("Sortkopp", sortkopp)

#   Tar verdien rød penn fra grønn kopp og flytter til hvit kopp
hvitkopp = grønnkopp
#   Tar verdien blå penn fra svart kopp og flytter til grønn kopp
grønnkopp = sortkopp
#   Tar verdien rød penn fra hvit kopp og flytter til svart kopp
sortkopp = hvitkopp

#   Skriv innholdet til grønnkopp til skjerm
print("\nGrønnkopp", grønnkopp)
#   Skriv innholdet til sortkopp til skjerm 
print("Sortkopp", sortkopp)
