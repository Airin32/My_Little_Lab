import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd= "Alpin123",
    database = "learning"
)

if db.is_connected():
    print("Berhasil terhubung ke database")

def show () :
    dt = db.cursor()
    dt.execute("select * from mahasiswa")
    data  = dt.fetchall()
    print("\t\tData Mahasiswa : \t\t")
    for i in data :
        print(i)
show()