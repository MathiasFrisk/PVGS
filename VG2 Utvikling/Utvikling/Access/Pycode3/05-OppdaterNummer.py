import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\MEDLEMSREGISTER.ACCDB;'
    conn = pyo.connect(con_string)

    medlemsID = 20
    mobil = "44444444"
    

    cursor = conn.cursor()

    cursor.execute("UPDATE Medlemmer SET mobil = ? WHERE medlemsID = ?", (mobil,medlemsID))
    cursor.commit()
    print("Data er oppdatert!")
    


except pyo.Error as e:
    print("Feil i kobling", e)    