from fungsiDasar import len
from fungsiBacacsv import matriks

def tukar(variabel,x):
    if variabel != "" :
        x = variabel
    else:
        x = x
    return x

data = matriks("game.csv")
perintah = input()
while perintah == "ubah_game":
    id_game = input("Masukkan ID game: ")
    a = 0
    for i in range (len(data)):
        if id_game in data[i][0]:
            a = 1
            nama = data[i][1]
            kategori = data[i][2]
            tahun_rilis = data[i][3]
            harga = data[i][4]

            nama_baru = input("Masukkan nama game: ")
            kategori_baru = input("Masukkan kategori: ")
            tahun_rilis_baru = input("Masukkan tahun rilis: ")
            harga_baru = input("Masukkan harga: ")

            #ubah nilai di csv -> pake F16_save    
            nama = tukar(nama_baru,nama)
            kategori = tukar(kategori_baru, kategori)
            tahun_rilis = tukar(tahun_rilis_baru, tahun_rilis)
            harga = tukar(harga_baru, harga)

            perintah = input()

        else:
            pass

    if a == 0:
        print("Tidak ada game dengan ID tersebut!")
        perintah = input()
