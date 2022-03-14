import pyodbc as pyo

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Code\Access\DB\MEDLEMSREGISTER.ACCDB;'
    conn = pyo.connect(con_string)

    cursor = conn.cursor()

    NyeMedlemmer = (
        (34,"Olsenbanden","Dyr", "Storgata 9","0421","48235537","25434895","Olsen99@gmail.com","10.3.2003",2,True),
        (35,"Sander","Lysa", "Heigata 9","0422","48533237","24454695","SanderLysa3@gmail.com","22.5.2010",1,False),
        (36,"Peder","Rasmus", "Gågaten 32","3194","48527247","24456745","Peder22222@gmail.com","27.2.2000",2,True),
    )

    cursor.executemany("INSERT INTO medlemmer VALUES (?,?,?,?,?,?,?,?,?,?,?)",NyeMedlemmer)
    conn.commit()
    
    print("Data lagt til!")



except pyo.Error as e:
    print("Feil: ",e)    