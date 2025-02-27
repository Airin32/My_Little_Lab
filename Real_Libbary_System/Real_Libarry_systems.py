import os 
import mysql.connector
os.system('cls')
sql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Alpin123",
    database = "belajar"
)
if sql.is_connected:
    print("Data SQL Terhubung")

class NEWBOOK :
    def __init__(self) -> None:
        self.__No = None
        self.__Judul = None 
        self.__Penulis = None 
        self.__Tanggal = None

    def Input (self) :
        self.__No = int(input("Masukan No Buku :"))
        self.__Judul = input("Masukan Judul Buku : ")
        self.__Penulis = input("Masukan Nama Penulis : ")
        self.__Tanggal = input("Tanggal Rilis : ")
    def save (self) :
        Data = sql.cursor()
        query =("INSERT INTO PERPUSTAKAAN (NO,JUDUL_BUKU,PENULIS,TANGGAL_RILIS) VALUES (%s,%s,%s,%s)")
        values = (self.__No,self.__Judul,self.__Penulis,self.__Tanggal)
        Data.execute(query,values)
        sql.commit()
    
    def show (self) :
        data = sql.cursor()
        data.execute("SELECT * FROM PERPUSTAKAAN ")
        data_buku = data.fetchall()
        for i in data_buku :
            print("|",i,"|")
    def change (self) :
        changer = sql.cursor()
        query = ("UPDATE PERPUSTAKAAN SET JUDUL_BUKU = (%s), PENULIS = (%s), TANGGAL_RILIS = (%s) WHERE NO = %s")
        values = (self.__Judul,self.__Penulis,self.__Tanggal,self.__No)
        changer.execute(query,values)
    
    def Book_list (self) :
        Book = [self.__No, self.__Judul, self.__Penulis,self.__Tanggal]
        return Book
    def __str__ (self) :
        return f"    | {self.__No} | {self.__Judul} | {self.__Penulis} | {self.__Tanggal}"

class VISSITER :

    def __init__(self) -> None:
        self.__Name = None 
        self.__Tanggal_Peminjam = None
        self.__lama = None 
        self.__seluruh_buku = [None]
        self.__jml = None 

    
    def Input (self) :
        self.__Name = input('Masukan Nama anda : ')
        self.__Tanggal_Peminjam =input("Tanggal Peminjaman : ")
        self.__jml = int(input("Jumlah Buku yang anda pinjam "))
        Jumlah = self.__jml
        buku = []
        for i in range(Jumlah) :
            self.__Buku = input ("Masukan Judul Buku yang anda pinjam :")
            buku.append(self.__Buku)
            self.__seluruh_buku = buku
        self.__lama = int(input("Lama Peminjaman : "))
    
    def Peminjam (self) :
        Orang = [self.__Name, self.__Tanggal_Peminjam, self.__jml,self.__seluruh_buku,self.__lama]
        return Orang 
    
    def __str__ (self) :
        return ("Nama Peminjam : {} \n Tanggal : {} \n Jumlah Buku : {} \n Judul buku  {} \n  Lama hari peminjaman : {} ".format (

            self.__Name,self.__Tanggal_Peminjam, self.__jml, self.__seluruh_buku,self.__lama)
        )
class DENDA :
    def __init__(self) -> None:
        self.__Nama = None 
        self.__Telat = None
        self.__jml_buku = None
        self.__Total_telat = None
        self.__Total_Hilang = None
        self.__Hilang = None   
    def Input (self) :
        self.__Nama = input("Masukan Nama : ")
        self.__Telat = int(input("Berapa lama anda Telat : "))
        self.__jml_buku = int(input("Masukan jumlah buku yang anda pinjam : "))
        telat = self.__Telat
        Jumlah_Buku = self.__jml_buku
        self.__Hilang = int(input("Berapa Buku yang anda Hilangkan :"))
        Hilang = self.__Hilang 
        if telat >= 7:
            self.__Total_telat = ((Jumlah_Buku * 5000) / 2 ) + ((telat // 7) * 5000  )
  
        if Hilang >= 1 :
            self.__Total_Hilang = Hilang * 45000
  
      
    def __str__ (self):
        return(f"Detail Pelanggar  : \n Nama : {self.__Nama} \n Telat : {self.__Telat} hari \n Jumlah Buku : {self.__jml_buku} \n Jumlah Buku yang Hilang : {self.__Hilang} \n Total Denda Buku yang Hilang : {self.__Total_Hilang} \n Total Denda Buku yan telat  : {self.__Total_telat} \n")

class Write_And_Read :
    def __init__(self,data) -> None:
        self.__data = data 
    
    def Save (self) :
        File_name = input("Masukan Nama file : ")
        Data = str(self.__data)
        with open (File_name, 'w', encoding="utf-8") as file :
            file.write(Data)
    def Load (self) :
        File_name = input("Masukan Nama File yang akan di tambah data : ")
        Data = str(self.__data)
        with open (File_name, 'a', encoding="utf-8") as file :
            file.write(Data)
        with open (File_name, 'a', encoding="utf-8") as file :
            file.write("\n")
    def Read (self) :
        Data = str (self.__data)
        with open (Data, 'r', encoding="utf-8") as file:
            print(file.read())
    def Read_line (self) :
        Data = str(self.__data)
        with open (Data, 'r', encoding="utf-8") as file :
            print(file.readline(),end="")
    def Read_all_lines (self) :
        Data = str(self.__data)
        with open (Data, 'r', encoding="utf-8") as file :
            print(file.readlines(),end="")
    
if __name__ == "__main__" :
    try : 
        while True :
            Tools = {
                1 : "Tambah Buku",
                2 : "Input pengunjung",
                3 : "Denda Pengunjung",
                4 : "Denda Perpustakaan",
            }
            for keys,values in Tools.items() :
                print(f"Pilih : {keys} untuk {values}")
            
            chouse = int(input("pilih operator : "))
            if chouse == 1 :
                Opsi = {
                    1 : "ADD Data",
                    2 : "Ubah Data"
                }
                for keys,values in Opsi.items():
                    print(f"Ketik  {keys} untuk {values}")
                ketik = int(input("Pilih Opsi :"))
                Atarashi_Hon = []
                Hon = NEWBOOK()
                print("="*20,"Buku Perpustakaan","="*20)
                Hon.show()
                if ketik == 1:
                    jml = int(input("Masukan Jumlah Buku :"))
                    for i in range (jml) :
                        hon = Hon.Input()
                        print(Hon.__str__())
                        Book = Hon.Book_list()
                        Atarashi_Hon.append(Book)
                        Hon.save()
                    print("NO    |Judul Buku      | Penulis         | Tanggal Rilis        |Genre        |")
                    for index,Atarashi in enumerate(Atarashi_Hon) :
                        print (f"{index} |{Atarashi[0]}    |{Atarashi[1]}       |{Atarashi[2]}       |{Atarashi[3]}   |")
                elif ketik == 2:
                    Delete_count = int(input("Masukan Jumlah data yang ingin diubah :"))
                    for i in range (Delete_count) :
                        Hon.Input()
                        Hon.change()
                    Hon.show()
            elif chouse == 2 :
                Kuru_no_hito = []
                PEOPLE = VISSITER()
                Data = Write_And_Read(PEOPLE)
                Make = input("Apakah data baru ingin Anda Buat ? (y/n) :")
                if Make == 'y' :
                    Data.Save()
                while (True) :
                    Hito = PEOPLE.Input()
                    print(PEOPLE.__str__())
                    Hito_list = PEOPLE.Peminjam()
                    Kuru_no_hito.append(Hito_list)
                    Data.Load()

                    stop = input("Apakah Pengunjung masih ada (y/n) : ")
                    if stop == 'n' :
                        break 

                print("NO   | Nama            |Tanggal Peminjaman    | Jumlah  | Judul                       |Lama peminjaman    |")
                for index,hito in enumerate(Kuru_no_hito) :
                    print(f"{index}   | {hito[0]}             | {hito[1]}                 |{hito[2]}   |{hito[3]}                            | {hito[4]} Hari|")
                    print(f"all data : {hito}")
            elif chouse == 3 :
                Denda =  DENDA()
                Data = Write_And_Read(Denda)
                data = input("Apakah anda akan membuat data baru ? (y/n) :")
                if data == 'y' :
                    Data.Save()
                Denda.Input()
                print(Denda.__str__())
                Data.Load()
                
            elif chouse == 4 :
                Libbary_data = {
                    1 : "Data Buku baru",
                    2 : "Data Pengunjung",
                    3 : "Data Denda"
                }
                for keys,values in Libbary_data.items():
                    print("pilih {} untuk membuka menu {}".format(keys,values))
                pilih = int(input("Silahkan pilih : "))
                if pilih == 1 :
                    Data = input("Masukan Nama data Yang akan di tampilkan : ")
                    Read = Write_And_Read(Data)
                    Read.Read()
                elif pilih == 2 :
                    Data = input("Masukan Nama Data yang akan di tampilkan : ")
                    read = Write_And_Read(Data)
                    read.Read()
                elif pilih == 3 :
                    Data = input("Masukan Nama Data yang akan ditampilkan : ")
                    read = Write_And_Read(Data)
                    read.Read()
            else :
                break
        raise ValueError("Program Terhenti")
    except ValueError as error :
        print("STATUS ERROR :  ",error)