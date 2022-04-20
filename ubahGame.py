import fungsiDasar as fd

def ubah_Nama (_indeks, _gameData):
    """ mengubah value field nama jika input tidak kosong """
    _variabel = input("Masukkan nama game: ")
    if _variabel != "":
        _gameData[_indeks][1] = _variabel
    else:
        pass
    return _gameData[_indeks][1]

def ubah_Kategori(_indeks, _gameData):
    """ mengubah value field kategori jika input tidak kosong """
    _variabel = input("Masukkan kategori: ")
    if _variabel != "":
        _gameData[_indeks][2] = _variabel
    else:
        pass
    return _gameData[_indeks][2]

def ubah_TahunRilis(_indeks, _gameData):
    """ mengubah value field tahun rilis jika input tidak kosong """
    _variabel = input("Masukkan tahun rilis: ")
    if _variabel != "":
        _gameData[_indeks][3] = _variabel
    else:
        pass
    return _gameData[_indeks][3]

def ubah_Harga(_indeks, _gameData):
    """ mengubah value field harga jika input tidak kosong """
    _variabel = input("Masukkan harga: ")
    if _variabel != "":
        _gameData[_indeks][4] = _variabel
    else:
        pass
    return _gameData[_indeks][4]

def ubahGame(_gameData):
    """ mengubah spesifikasi data game """
    _idGame = input("Masukkan ID game: ")
    if _idGame == "":
        print("Field ID harus diisi!")
    else:
        _cekGame = 0
        for i in range (1, fd.len(_gameData)):
            if _idGame == _gameData[i][0]:
                _cekGame = 1

                #ubah nilai di csv -> pake F16_save    
                ubah_Nama(i, _gameData)
                ubah_Kategori(i, _gameData)
                ubah_TahunRilis(i, _gameData)
                ubah_Harga(i, _gameData)  

                return _gameData

            else:
                pass

        if _cekGame == 0:
            print()
            print("Tidak ada game dengan ID tersebut!")
