import fungsiDasar as fd

def ubahStok(_gameData):
    id_game = input("Masukkan ID game: ")
    cek_game = 0
    for i in range (fd.len(_gameData)):
        if id_game == _gameData[i][0]:
            cek_game = 1
            stok = _gameData[i][5]
            nama = _gameData[i][1]
            ubah = int(input("Masukkan jumlah: "))
            totalstok = int(stok) + ubah
            if totalstok >= 0:
                if ubah<0:
                    print("Stok game", nama, "berhasil dikurangi. Stok sekarang:", totalstok)
                    _gameData[i][5] = totalstok
                else: #ubah>0
                    print("Stok game", nama, "berhasil ditambah. Stok sekarang:", totalstok)
                    _gameData[i][5] = totalstok
            else: #totalstok<0
                print("Stok game", nama, "gagal dikurangi karena stok kurang. Stok sekarang:", stok)

            return _gameData
        
        else:
            pass
    
    if cek_game == 0:
        print("Tidak ada game dengan ID tersebut!")
        
