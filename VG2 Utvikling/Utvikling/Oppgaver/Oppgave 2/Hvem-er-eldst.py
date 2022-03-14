# lag to variabeler som heter Henrik, Kari
henrik = input("Henrik sin alder: ")
kari = input("Kari sin alder: ")

# if setning som sier: hvis kari sin verdi er høyere enn henrik så printer den "Kari er eldre"
# elif setning som sier: hvis henrik sin verdi er høyere enn kari så printer den "Henrik er eldre"
# else setning som sier: hvis de er like alder så printer den "Henrik og Kari er like gamle"
if int(kari) > int(henrik):
    print("Kari er eldre")

elif int(kari) < int(henrik):
    print("henrik er eldre")
    
else:
    print("er like gamle")
