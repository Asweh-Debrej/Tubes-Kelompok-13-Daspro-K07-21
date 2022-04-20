import fungsiDasar as fd
import bacacsv as baca
import ubahGame as ug
import exit

def ubahStok(_gameData):
    """ mengubah data stok game """
    _idGame = input("Masukkan ID game: ")
    if _idGame == "":
        print("Field ID harus diisi!")
    else:
        _cekGame = 0
        for i in range (1, fd.len(_gameData)):
            if _idGame == _gameData[i][0]:
                _cekGame = 1
                _stok = _gameData[i][5]
                _nama = _gameData[i][1]
                _ubah = int(input("Masukkan jumlah: "))
                _totalStok = int(_stok) + _ubah
                if _totalStok >= 0:
                    if _ubah<0:
                        print("Stok game", _nama, "berhasil dikurangi. Stok sekarang:", _totalStok)
                        _gameData[i][5] = _totalStok
                    else: #ubah>0
                        print("Stok game", _nama, "berhasil ditambah. Stok sekarang:", _totalStok)
                        _gameData[i][5] = _totalStok
                else: #totalstok<0
                    print("Stok game", _nama, "gagal dikurangi karena stok kurang. Stok sekarang:", _stok)

                return _gameData
            
            else:
                pass
    
        if _cekGame == 0:
            print("Tidak ada game dengan ID tersebut!")
        
matriks1 = baca.matriks("game.csv")
matriks2 = baca.matriks("user.csv")
matriks3 = baca.matriks("kepemilikan.csv")
matriks4 = baca.matriks("riwayat.csv")
ubahStok(matriks1)
ug.ubahGame(matriks1)
exit.exit(matriks2, matriks1, matriks4, matriks3)

"""id;nama;kategori;tahun_rilis;harga;stok;
G001;Call of Duty;FPS;2000;1000;2;
G002;Elder Ring;Adventure;2020;2000;3;
G003;AC Unity;Adventure;2030;3000;4;"""