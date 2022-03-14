from msilib.schema import Error
import pyodbc as pyo

print("(1) Søk på vare-nr\n")
print("(2) Søk etter kategori\n")
print("(3) Register en ny vare\n")
print("(4) Oppdatere pris på en vare\n")
print("(5) Slett en vare\n")
print("- - - - - - - - - - - - - - - - - - - -\n")

brukerinput = int(input("velg hva du vil gjøre noe med: "))

if brukerinput == 1:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)

    print("------------ Søk etter vare-nr ------------\n")

    cursor = conn.cursor()
    varenr = int(input("Tast inn et vare-nr: "))
    cursor.execute("SELECT * FROM varer WHERE Nr = ?", (varenr))

    for row in cursor.fetchall():
        print(row)
    
    
elif brukerinput == 2:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)

    print("------------ Søk etter kategori ------------\n")

    cursor = conn.cursor()
    kategori = (input("Søk etter en Matvare: "))
    cursor.execute("SELECT * FROM varer WHERE kategori = ?", (kategori))

    for row in cursor.fetchall():
        print(row)

elif brukerinput == 3:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)

    cursor = conn.cursor()

    nr1 = int(input("Velg hvilket varenr: "))
    navn = (input("Hva heter varen: "))
    kategori2 = (input("Hvilken kategori går den under?: "))
    pris = int(input("Velg en pris: "))

    cursor.execute("INSERT INTO varer VALUES (?,?,?,?)",nr1,navn,kategori2,pris)
    conn.commit()
    
    print("Data lagt til!")   

elif brukerinput == 4:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)

    varenr2 = int(input("Velg hvilket varenr: "))
    Nypris2 = int(input("Ny pris på vare: "))
    

    cursor = conn.cursor()

    cursor.execute("UPDATE varer SET pris = ? WHERE Nr = ?", (Nypris2,varenr2))
    cursor.commit()
    print("Data er oppdatert!")

elif brukerinput == 5:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)

    cursor = conn.cursor()

    varenr3 = int(input("Velg hvilket varenr: "))

    cursor.execute(f"DELETE FROM varer WHERE varenr3 = {varenr3}")
    cursor.commit()
    print("Data slettet!")