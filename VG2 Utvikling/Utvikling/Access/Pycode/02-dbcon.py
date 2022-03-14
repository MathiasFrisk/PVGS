from msilib.schema import Error
import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Code\Access\DB\varer.accdb;'
    conn = pyo.connect(con_string)
    print("Koblet til databasen!")


except pyo.Error as e:
    print("Feil i kobling: ",e)