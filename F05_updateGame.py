import C01_fungsiDasar as fd

def ubah_value(_indeks, _gameData, _variabel, j):
    """ mengubah value field j jika input tidak kosong """
    if _variabel != "":
        _gameData[_indeks][j] = _variabel
    
    return _gameData[_indeks][j]

def ubahGame(_gameData):
    # mengubah spesifikasi data game
    _idGame = input("Masukkan ID game: ")
    if _idGame == "": 
        print("Field ID harus diisi!")
    else:
        _cekGame = 0
        for i in range (1, fd.len(_gameData)):
            if _idGame == _gameData[i][0]:
                _cekGame = 1

                _namaBaru = input("Masukkan nama game: ")
                _kategoriBaru = input("Masukkan kategori: ")
                _tahunRilisBaru = input("Masukkan tahun rilis: ")
                _hargaBaru = input("Masukkan harga: ")

                # mengubah value field spesifikasi data game sesuai input yang diberikan   
                ubah_value(i, _gameData, _namaBaru, 1)
                ubah_value(i, _gameData, _kategoriBaru, 2)
                ubah_value(i, _gameData, _tahunRilisBaru, 3)
                ubah_value(i, _gameData, _hargaBaru, 4)

                return _gameData
        
        if _cekGame == 0:  # input id game tidak valid
            print()
            print("Tidak ada game dengan ID tersebut!")

