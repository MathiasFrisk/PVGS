# forkorte pandas til pd

import pandas as pd

mat = pd.read_csv("mat-pris.csv", sep=";", encoding= "latin-1")


print("-----------------")

print("Oppgave 1")

#1 

print(mat.columns)

print("-----------------")

print("Oppgave 2")

#2

print(mat.head(4))

print("-----------------")

print("Oppgave 3")

#3 

print(mat.tail(4))

#4

print("-----------------")

print("Oppgave 4")

print(mat[mat.Kategori== 'Melk' ])

#5
print("-----------------")

print("Oppgave 5")

print(mat.loc[mat.ID==222, :])

#6
print("-----------------")

print("Oppgave 6")

print(mat.loc[mat.ID==221, ["ID", "Kategori"]])
mat.loc[mat.ID==221, "Kategori"] = "Fe"
print(mat.loc[mat.ID==221, ["ID", "Kategori"]])

#7
print("-----------------")

print("Oppgave 7")

print(mat.loc[mat.ID==222, ["ID", "Pris"]])
mat.loc[mat.ID==222, "Pris"] = "100"
print(mat.loc[mat.ID==222, ["ID", "Pris"]])

#8

print("-----------------")
"""
print("Oppgave 8")

print(mat.loc[mat.ID==Fe, ["ID", "Pris"]])
mat.loc[mat.ID==Fe, "Pris"] * 1.5
print(mat.loc[mat.ID==Fe, ["ID", "Pris"]])
"""
mat.to_csv("ny_mat-pris.csv", index=False)