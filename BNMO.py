import fungsiDasar as fd
import fungsiBuatan as fb
import register as reg
import login
import addGame as ag
import ubahGame as ug
import ubahStok as us
import listingGame as lg
import Fungsi10 as F10
import Fungsi11 as F11
import beliGame as bg
import lihatGameSudahDibeli as lgsd
import topup
import history
import help
import exit
import save as sv
import Fungsi15Load as loading
import cipher as cp
import magicConchShell as mcs
import tictactoe as tt


_role = "user"
_loggedIn = False
_adminCmds = ["register", "login", "tambahgame", "ubahgame", "ubahstok", "listgametoko", "searchgameatstore", "topup", "help", "save", "exit"]
_userCmds = ["login", "listgametoko", "buygame", "listgame", "searchmygame", "searchgameatstore", "riwayat", "help", "save", "exit"]
_valCommand = fb.merge(_adminCmds, _userCmds)


_loggedUser = ["1", "2", "3", "4", "5", 0]
"""Data user yang telah login
1 : id
2 : username
3 : nama
4 : password
5 : role (admin/user)
6 : saldo
"""


_usersData = [["1", "2", "3", "4", "5", 0]]
"""Diimport dari user.csv sebagai variabel global
1 : id
2 : username
3 : nama
4 : password
5 : role (admin/user)
6 : saldo
"""

_gameData = [["1", "2", "3", 2000, 0, 0]]
"""Diimport dari game.csv sebagai variabel global
1 : id
2 : nama
3 : kategori
4 : tahun rilis
5 : harga
6 : stok
"""

_history = [["1", "2", 0, "4", 2000]]
"""Diimport dari riwayat.csv sebagai variabel global
1 : id game
2 : nama game
3 : harga game
4 : id pembeli
5 : tahun pembelian
"""

_possession = [["1", "2"]]
"""Diimport dari kepemilikan.csv sebagai variabel global
1 : id game
2 : id pemilik
"""


def roleCmdIsValid(role, command, adminCmds, userCmds):
    """ validasi command sesuai role """
    cek_command = False
    if role == "admin":
        if fd.find(adminCmds, command) != -1:
            cek_command = True
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')
    else: #_role == "user"
        if fd.find(userCmds, command) != -1:
            cek_command = True
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')

    return cek_command


def mintaCommand():
    global _role, _loggedIn, _usersData, _gameData, _history, _possession, running, _loggedUser
    command = fd.replace(fd.replace(fd.replace(input(">>> ").lower(), ' ', ''), '_', ''), '-', '')     # Toleransi bagi pengguna yang menggunakan (' '), ('_'), atau ('-') sebagai pengutaraan maksud perintah
    if fd.find(_valCommand, command) != -1:                 # validasi input command
        if _loggedIn:
            if roleCmdIsValid(_role, command, _adminCmds, _userCmds):              # validasi perintah admin dan user
                if command == "register":
                    _usersData = reg.register(_usersData)
                elif command == "login":
                    print('Anda sudah login! Untuk melihat list command, ketik "help".')
                elif command == "tambahgame":
                    _gameData = ag.addGame(_gameData)
                elif command == "ubahgame":
                    ug.ubahGame(_gameData)
                elif command == "ubahstok":
                    us.ubahStok(_gameData)
                elif command == "listgametoko":           # Melihat daftar game yang ada     
                    lg.listing_game(_gameData)
                elif command == "buygame":
                    _wanted = input("Masukkan ID Game: ")   # Membeli game
                    if(bg.beli(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)):
                        _history     = bg._ubahHistory(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                        _gameData    = bg._ubahGameData(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                        _loggedUser  = bg._ubahLoggedUsers(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                        _usersData   = bg._ubahUsersData(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                        _possession  = bg._ubahPossession(_wanted, _loggedUser, _possession, _gameData, _usersData, _history) 
                elif command == "listgame":
                    lgsd.lihat(_loggedUser[0],_gameData,_possession)            # melihat daftar game yang dimiliki 
                elif command == "searchmygame":
                    F10.search_my_game(_possession,_gameData,_loggedUser)
                elif command == "searchgameatstore":
                    F11.search_game_at_store(_gamedata)
                elif command == "riwayat":
                    history.history(_gameData, _loggedUser)
                elif command == "topup":
                    _usersData = topup.topup(_usersData)
                elif command == "help":
                    help.help(_role)
                elif command == "exit":
                    running = exit.exit(_usersData, _gameData, _history, _possession)
                elif command == "save":
                    cari = input("Masukkan nama folder penyimpanan : ")         # Melakukan save
                    print("")
                    print("Saving")
                    sv.simpan(_possession,"kepemilikan",cari)
                    sv.simpan(_gameData,"game",cari)
                    sv.simpan(_usersData,"user",cari)
                    sv.simpan(_history,"riwayat",cari)
                    print("Data telah disimpan pada folder " + cari +"!")
                    
                elif command == "kerangajaib":
                    mcs.kerangAjaib()                       # Kerang Ajaib
            else: # command tidak valid dengan _role
                pass

        else: #_loggedIn = False
            if command == "login":
                _loggedUser = login.login(_usersData)
                if _loggedUser != None: #username dan password sudah tervalidasi
                    _role = _loggedUser[4]
                    _loggedIn = True
            elif command == "help":
                help.help(_role)                         
            else:
                # validasi perintah, tidak boleh melakukan apa-apa sebelum login KECUALI HELP
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    
    else: #command != _valCommand[i]
        print('Command tidak ada. Untuk melihat list command, ketik "help".')
        
                


running = True



if __name__ == "__main__":   # Inti program
    loading.load()
    while running:
        mintaCommand()

    print("Selamat menikmati hari anda :(")
