import datetime


bt_hp = ["Gulsetsenteret","Ravnåsen","Myren","Skien Landmannstorget","Rådhusplassen","Bøle","Borgestad","Porsgrunn Kammerherreløkka"]
bt_t = [0,6,11,16,17,21,25,35]

print("\nNy bussrute fra Gulset (M1)")
time = input("Oppgi start i timer: ")
minutter = input("Oppgi start i minutter: ")
print("Start tiden er:", time,":",minutter,"\n")

print("Avgang fra", *bt_hp, sep = "\n")