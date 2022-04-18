import fungsiDasar as fd

def exit():
    confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")
    while fd.find(['y', 'n', 'yes', 'no', 'ya', 'tidak'], confirm.lower()) == -1:
        print("Masukan tidak sesuai!")
        confirm = input("Apakah anda benar benar ingin keluar? (Y/n) ")

    if fd.find(['n', 'no', 'tidak'], confirm.lower()):
        return 1            # tidak jadi keluar

    save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")
    while fd.find(['y', 'n', 'yes', 'no', 'ya', 'tidak'], save.lower()) == -1:
        print("Masukan tidak sesuai!")
        save = input("Apakah Anda ingin menyimpan perubahan yang telah dibuat? (Y/n) ")

    if fd.find(['y', 'yes', 'ya'], save.lower()):
        pass        #------------------------------------------------------------- save
    
    return 0                # program ditutup