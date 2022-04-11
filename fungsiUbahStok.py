from fungsiDasar import len
from fungsiBacacsv import matriks

data = matriks("game.csv")
perintah = input()
while perintah == "ubah_stok":
    id_game = input("Masukkan ID game: ")
    a = 0
    for i in range (len(data)):
        if id_game in data[i][0]:
            a = 1
            stok = data[i][5]
            nama = data[i][1]
            ubah = int(input("Masukkan jumlah: "))
            totalstok = int(stok) + ubah
            if totalstok >= 0:
                if ubah<0:
                    print("Stok game", nama, "berhasil dikurangi. Stok sekarang:", totalstok)
                    stok = totalstok #ubah nilai di csv -> pake F16_save
                    print(stok)
                    perintah = input()
                else: # ubah>0
                    print("Stok game", nama, "berhasil ditambah. Stok sekarang:", totalstok)
                    stok = totalstok #ubah nilai di csv -> pake F16_save
                    print(stok)
                    perintah = input()
            else: # totalstok <0
                print("Stok game", nama, "gagal dikurangi karena stok kurang. Stok sekarang:", stok)
                perintah = input()
        else:
            pass

    if a == 0:
        print("Tidak ada game dengan ID tersebut!")
        perintah = input()
