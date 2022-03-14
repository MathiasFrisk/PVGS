import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\MEDLEMSREGISTER.ACCDB;'
    conn = pyo.connect(con_string)
    print('Koblet til database!')

except pyo.Error as e:
    print("Feil i kobling: ", e)

    