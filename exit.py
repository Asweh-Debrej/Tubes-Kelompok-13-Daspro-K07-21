def exit():
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
        pass        #------------------------------------------------------------- save
    
    return 0                # program ditutup