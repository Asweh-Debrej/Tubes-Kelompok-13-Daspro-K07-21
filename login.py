import fungsiDasar as fd

def login(_usersData):
    """ validasi input username dan password ketika login """
    in_username = input("Masukkan username: ")
    in_password = input("Masukkan password: ")
    cek_valid = 0
    _loggedUser = ["0","1","2","3","4","5"]
    for i in range(fd.len(_usersData)):
        if in_username == _usersData[i][1]:
            if in_password == _usersData[i][3]:
                cek_valid = 1

                # mengambil data user/admin yang login dan memindahkan data ke list _loggedUser
                _loggedUser[0] = _usersData[i][0]
                _loggedUser[1] = _usersData[i][1] 
                _loggedUser[2] = _usersData[i][2]
                _loggedUser[3] = _usersData[i][3]
                _loggedUser[4] = _usersData[i][4]
                _loggedUser[5] = _usersData[i][5]

                print('Halo', _loggedUser[2], '! Selamat datang di "Binomo".')
            
                return _loggedUser

            else:
                pass
        else:
            pass

    if cek_valid == 0:
        print("Password atau username salah atau tidak ditemukan.")

def admin(x):
    """" command yang valid untuk admin """
    cek = True
    if x == "register" or x == "login" or x == "tambah_game" or x == "ubah_game" or x == "ubah_stok" or x == "list_game_toko" or x == "search_game_at_store" or x == "topup" or x == "help" or x == "save" or x == "exit":
        cek = True
    else:
        cek = False
    return cek

def user(x):
    """ command yang valid untuk user """
    cek = True
    if x == "login" or x == "list_game_toko" or x == "buy_game" or x == "list_game" or x == "search_my_game" or x == "search_game_at_store" or x == "riwayat" or x == "help" or x == "save" or x == "exit":
        cek = True
    else:
        cek = False
    return cek

def isValid(_role, command):
    """ validasi command sesuai _role """
    cek_command = False
    if _role == "admin":
        if admin(command):
            cek_command = True
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.") 
            print('Untuk melihat list command, ketik "help"')
    else: #_role == "user"
        if user(command):
            cek_command = True
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')

    return cek_command
