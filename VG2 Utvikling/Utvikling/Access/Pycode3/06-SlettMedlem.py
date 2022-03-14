import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\MEDLEMSREGISTER.ACCDB;'
    conn = pyo.connect(con_string)

    cursor = conn.cursor()

    medlemsID = 10

    cursor.execute(f"DELETE FROM Medlemmer WHERE MedlemsID = {medlemsID}")
    cursor.commit()
    print("Data slettet!")


except pyo.Error as e:
    print("Feil i kobling", e)    