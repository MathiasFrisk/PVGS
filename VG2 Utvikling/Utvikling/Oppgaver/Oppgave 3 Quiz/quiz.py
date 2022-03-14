# lag en variabel som heter poeng med verdien 0
poeng = 0
# skriv til skjerm at du har startet quizen
print("Du har startet quizen\n")
# skriv til skjerm hva er 2 + 2
print("Spørsmål 1: Hva er 2+2?")
# hvis oppgitt svar = 4
svar = input("ditt svar: ")
#   skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar.lower() == "4":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm Hva heter kongen av norge
print("Spørsmål 2: Hva heter kongen av norge?")
# hvis oppgitt svar = Harald
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar.lower() == "harald":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm Hvem er Joe Biden
print("Spørsmål 3: Hvem er Joe Biden?")
# hvis oppgitt svar = President
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
if svar.lower() == "president":
    print("Riktig\n")
    poeng += 1
#       øk med poengsum 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm Hvem er statsminister i norge
print("Spørsmål 4: Hvem er statsminister i norge?")
# hvis oppgitt svar = Erna
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar.lower() == "erna":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm når startet 2 verdenskrig
print("Spørsmål 5: Når startet 2 verdenskrig?")
# hvis oppgitt svar = 1939
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "1939":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm når sluttet 2 verdenskrig? 
print("Spørsmål 6: Når sluttet 2 verdenskrig?")
# hvis oppgitt svar = 1945
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "1945":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm når ble fortnite lansert 
print("Spørsmål 7: Når ble fortnite lansert?")
# hvis oppgitt svar = 2017
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "2017":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm hvilket år er det nå?
print("Spørsmål 8: hvilket år er det nå?")
# hvis oppgitt svar = 2021
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "2021":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm Hva er 2+3? 
print("Spørsmål 9: Hva er 2+3?")
# hvis oppgitt svar = 5
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "5":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm Hva er 4+3? 
print("Spørsmål 10: Hva er 4+3? ")
# hvis oppgitt svar = 7
svar = input("ditt svar: ")
# skriv til skjerm at svaret er "riktig" 
#       øk med poengsum 1
if svar == "7":
    print("Riktig\n")
    poeng += 1
# ellers
#   skriver til skjerm at det er "feil"
else:
    print("Feil\n")

# skriv til skjerm total poengsum
print("Du fikk",poeng, "av 10 poeng")