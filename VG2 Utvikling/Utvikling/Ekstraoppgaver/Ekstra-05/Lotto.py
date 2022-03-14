# import random
import random
# skriv til skjerm at du har startet lotto
print("----------- Du har startet lotto -----------")
#lag en variabel som heter antallforsøk med veriden 0
antallforsøk = 0
antall_rette = 0

# lag en whileløkke som går for vær gang tallet er likt 

# lag en whileløkke som lager vinner tallene

vt1 = random.randint(1, 34)
vt2 = random.randint(1, 34)
while vt1==vt2: 
    vt2 = random.randint(1, 34)

vt3 = random.randint(1, 34)
while vt3==vt1 or vt3==vt2: 
    vt3 = random.randint(1, 34)

vt4 = random.randint(1, 34)
while vt4==vt1 or vt4==vt2 or vt4==vt3: 
    vt4 = random.randint(1, 34)

vt5 = random.randint(1, 34)
while vt5==vt1 or vt5==vt2 or vt5==vt3 or vt5==vt4: 
    vt5 = random.randint(1, 34)

vt6 = random.randint(1, 34)
while vt6==vt1 or vt6==vt2 or vt6==vt3 or vt6==vt4 or vt6==vt5:  
    vt6 = random.randint(1, 34)

vt7 = random.randint(1, 34)
while vt7==vt1 or vt7==vt2 or vt7==vt3 or vt7==vt4 or vt7==vt5 or vt7==vt6:   
    vt7 = random.randint(1, 34)



#brukerstallsortert = sorted(brukerstall)
#print(brukerstallsortert)


#vinnerbrukerstallsortert = sorted(vinnerbrukerstall)
#print("----- Vinner tall -----")
#print(vinnerbrukerstallsortert)

while brukerstall != vinnerbrukerstall :
    
    antall_rette = 0
    tt1 = random.randint(1, 34)
    tt2 = random.randint(1, 34)
    antallforsøk+=1

    while tt1==tt2: 
        tt2 = random.randint(1, 34)

    tt3 = random.randint(1, 34)
    while tt3==tt1 or tt3==tt2: 
        tt3 = random.randint(1, 34)

    tt4 = random.randint(1, 34)
    while tt4==tt1 or tt4==tt2 or tt4==tt3: 
        tt4 = random.randint(1, 34)

    tt5 = random.randint(1, 34)
    while tt5==tt1 or tt5==tt2 or tt5==tt3 or tt5==tt4: 
        tt5 = random.randint(1, 34)

    tt6 = random.randint(1, 34)
    while tt6==tt1 or tt6==tt2 or tt6==tt3 or tt6==tt4 or tt6==tt5:  
        tt6 = random.randint(1, 34)

    tt7 = random.randint(1, 34)
    while tt7==tt1 or tt7==tt2 or tt7==tt3 or tt7==tt4 or tt7==tt5 or tt7==tt6:   
        tt7 = random.randint(1, 34)

if tt1 == vt1 or tt1 == vt2 or tt1 == vt3 or tt1 == vt4 or tt1 == vt5 or tt1 == vt6 or tt1 == vt7:
    antall_rette += 1 

if tt2 == vt1 or tt2 == vt2 or tt2 == vt3 or tt2 == vt4 or tt2 == vt5 or tt2 == vt6 or tt2 == vt7:
    antall_rette += 1 

if tt3 == vt1 or tt3 == vt2 or tt3 == vt3 or tt3 == vt4 or tt3 == vt5 or tt3 == vt6 or tt3 == vt7:
    antall_rette += 1

if tt4 == vt1 or tt4 == vt2 or tt4 == vt3 or tt4 == vt4 or tt4 == vt5 or tt4 == vt6 or tt4 == vt7:
    antall_rette += 1

if tt5 == vt1 or tt5 == vt2 or tt5 == vt3 or tt5 == vt4 or tt5 == vt5 or tt5 == vt6 or tt5 == vt7:
    antall_rette += 1

if tt6 == vt1 or tt6 == vt2 or tt6 == vt3 or tt6 == vt4 or tt6 == vt5 or tt6 == vt6 or tt6 == vt7:
    antall_rette += 1 

if tt2 == vt1 or tt7 == vt2 or tt7 == vt3 or tt7 == vt4 or tt7 == vt7 or tt7 == vt6 or tt7 == vt7:
    antall_rette += 1 


    brukerstall = (tt1,tt2,tt3,tt4,tt5,tt6,tt7)     
    vinnerbrukerstall = (vt1,vt2,vt3,vt4,vt5,vt6,vt7)  

    print(brukerstall)    

    if brukerstall == vinnerbrukerstall:
        print("Det tok",antallforsøk,"forsøk til å kunne få lotto.")
        print("Brukerstall:",brukerstall)
        print("Vinnerstall",vinnerbrukerstall)   
