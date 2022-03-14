liste_a = ["svein, Thore, Ove"]
print(liste_a)
print(type(liste_a))
print(len(liste_a))

liste_b = []
liste_b.append("Hanne")
liste_b.append("Kåre")
print(liste_b)

liste_a.append("Thore")
print(liste_a)
print(liste_a[-1])

liste_a[1] = "tore"
print(liste_a)

liste_a.remove("Thore")
print(liste_a)

navn = "Mathias"
print(navn[3])