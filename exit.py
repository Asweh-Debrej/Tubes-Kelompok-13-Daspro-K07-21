import save as sv

def exit(_usersData, _gameData, _history, _possession):
    confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")
    while confirm.lower() not in ['y', 'n', 'yes', 'no', 'ya', 'tidak']:
        print("Masukan tidak sesuai!")
        confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")

    if confirm.lower() in ['n', 'no', 'tidak']:
        return 1            # tidak jadi keluar

    save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")
    while save.lower() not in ['y', 'n', 'yes', 'no', 'ya', 'tidak']:
        print("Masukan tidak sesuai!")
        save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")

    if save.lower() in ['y', 'yes', 'ya']:
        cari = input("Masukkan nama folder penyimpanan : ")
        print("")
        print("Saving")
        sv.simpan(_possession, "kepemilikan", cari)
        sv.simpan(_gameData, "game", cari)
        sv.simpan(_usersData, "user", cari)
        sv.simpan(_history, "riwayat", cari)
        print("Data telah disimpan pada folder " + cari + "!")
    
    return 0                # program ditutup
