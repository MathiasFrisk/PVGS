import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\MEDLEMSREGISTER.ACCDB;'
    conn = pyo.connect(con_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medlemmer WHERE Fødseldato BETWEEN '13.03.1975' and '10.03.2003'")

    for rad in cursor.fetchall():
        print(rad)


except pyo.Error as e:
    print("Feil i kobling", e)    


#Ikke Ferdig