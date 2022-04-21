import fungsiDasar as fd
import save as sv

def exit(_usersData, _gameData, _history, _possession, loggedIn):
    if not loggedIn:
        return 0
        
    confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")
    while fd.find(['y', 'n', 'yes', 'no', 'ya', 'tidak'], confirm.lower()) == -1:
        print("Masukan tidak sesuai!")
        confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")

    if fd.find(['n', 'no', 'tidak'], confirm.lower()) != -1:
        return 1            # tidak jadi keluar

    save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")
    while fd.find(['y', 'n', 'yes', 'no', 'ya', 'tidak'], save.lower()) == -1:
        print("Masukan tidak sesuai!")
        save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")

    if fd.find(['y', 'yes', 'ya'], save.lower()) != -1:
        cari = input("Masukkan nama folder penyimpanan : ")
        print("")
        print("Saving")
        sv.simpan(_possession, "kepemilikan", cari)
        sv.simpan(_gameData, "game", cari)
        sv.simpan(_usersData, "user", cari)
        sv.simpan(_history, "riwayat", cari)
        print("Data telah disimpan pada folder " + cari + "!")
    
    return 0                # program ditutup
