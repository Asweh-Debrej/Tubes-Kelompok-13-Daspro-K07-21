import fungsiDasar as fd
import cipher as cp

def login(_usersData):
    # menerima dan memvalidasi input username dan input password agar dapat mengakses binomo
    _inUsername = input("Masukkan username: ")
    _inPassword = cp.cipher(input("Masukkan password: "))
    _cekValid = 0
    # menginisiasi list _loggedUser
    _loggedUser = ["0","1","2","3","4","5"]
    for i in range(1, fd.len(_usersData)):
        if _inUsername == _usersData[i][1]:
            if _inPassword == _usersData[i][3]:
                _cekValid = 1

                # mengambil data user/admin yang login dan memindahkan data ke list _loggedUser
                _loggedUser[0] = _usersData[i][0]
                _loggedUser[1] = _usersData[i][1] 
                _loggedUser[2] = _usersData[i][2]
                _loggedUser[3] = _usersData[i][3]
                _loggedUser[4] = _usersData[i][4]
                _loggedUser[5] = _usersData[i][5]

                print('Halo', _loggedUser[2], '! Selamat datang di "Binomo".')
                print("Anda memiliki saldo sebesar", _loggedUser[5])
            
                return _loggedUser

    if _cekValid == 0: # input username atau password tidak valid
        print("Password atau username salah atau tidak ditemukan.")
