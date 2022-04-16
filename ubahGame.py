import fungsiDasar as fd

def ubah_Nama (indeks, _gameData):
    """ mengubah value field nama jika input tidak kosong """
    variabel = input("Masukkan nama game: ")
    if variabel != "":
        _gameData[indeks][1] = variabel
    else:
        pass
    return _gameData[indeks][1]

def ubah_Kategori(indeks, _gameData):
    """ mengubah value field kategori jika input tidak kosong """
    variabel = input("Masukkan kategori: ")
    if variabel != "":
        _gameData[indeks][2] = variabel
    else:
        pass
    return _gameData[indeks][2]

def ubah_TahunRilis(indeks, _gameData):
    """ mengubah value field tahun rilis jika input tidak kosong """
    variabel = input("Masukkan tahun rilis: ")
    if variabel != "":
        _gameData[indeks][3] = variabel
    else:
        pass
    return _gameData[indeks][3]

def ubah_Harga(indeks, _gameData):
    """ mengubah value field harga jika input tidak kosong """
    variabel = input("Masukkan harga: ")
    if variabel != "":
        _gameData[indeks][4] = variabel
    else:
        pass
    return _gameData[indeks][4]

def ubahGame(_gameData):
    #ganti game
    id_game = input("Masukkan ID game: ")
    if id_game == "":
        print("Field ID harus diisi!")
    else:
        cek_game = 0
        for i in range (fd.len(_gameData)):
            if id_game == _gameData[i][0]:
                cek_game = 1

                #ubah nilai di csv -> pake F16_save    
                ubah_Nama(i, _gameData)
                ubah_Kategori(i, _gameData)
                ubah_TahunRilis(i, _gameData)
                ubah_Harga(i, _gameData)  

                return _gameData

            else:
                pass

        if cek_game == 0:
            print("")
            print("Tidak ada game dengan ID tersebut!")
