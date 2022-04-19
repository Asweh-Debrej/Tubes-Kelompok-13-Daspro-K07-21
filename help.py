def help(_role):
    """ mengeluarkan list command berdasarkan _role """
    if _role == "admin": #fungsi yg hanya bisa diakses admin
        print("============ HELP ===========")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("5. ubah_game - Untuk mengubah informasi game dengan informasi baru")
        print("6. ubah_stok - Untuk mengubah stok sebuah game pada toko")
        print("7. search_game_at_store - Untuk mendapatkan informasi game yang ada di toko")
        print("8. topup - Untuk menambahkan saldo kepada user")
        print("9. help - Untuk memberikan panduan penggunaan sistem")
        print("10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
        print("11. exit - Untuk keluar dari aplikasi")
    else: # _role == "user"
        print("============ HELP ===========")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. buy_game - Untuk membeli game")
        print("4. list_game - Untuk melihat daftar game yang dimiliki pengguna")
        print("5. search_my_game - Untuk mendapatkan informasi game pada inventory")
        print("6. search_game_at_store - Untuk mendapatkan informasi game yang ada di toko")
        print("7. riwayat - Untuk melihat riwayat pembelian game")
        print("8. help - Untuk memberikan panduan penggunaan sistem")
        print("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
        print("10. exit - Untuk keluar dari aplikasi")
