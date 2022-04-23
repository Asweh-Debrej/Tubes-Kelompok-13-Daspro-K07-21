import fungsiDasar as fd

def ubahStok(_gameData):
    # mengubah data stok game
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
                if _ubah == "":
                    print("Jumlah tidak ada! Silakan coba lagi.")
                else: 
                    _totalStok = _stok + _ubah
                    if _totalStok >= 0:
                        if _ubah<0:
                            print("Stok game", _nama, "berhasil dikurangi. Stok sekarang:", _totalStok)
                            _gameData[i][5] = _totalStok
                        else: # ubah>0
                            print("Stok game", _nama, "berhasil ditambah. Stok sekarang:", _totalStok)
                            _gameData[i][5] = _totalStok
                    else: # totalstok<0
                        print("Stok game", _nama, "gagal dikurangi karena stok kurang. Stok sekarang:", _stok)

                    return _gameData
        
        if _cekGame == 0:  # input id game tidak valid
            print()
            print("Tidak ada game dengan ID tersebut!")
