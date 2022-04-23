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
import os # design (pake cls)


_role = "user"
_loggedIn = False
_adminCmds = ["register", "login", "addgame", "updategame", "updatestock", "store", "storesearch", "topup", "help", "save", "exit","magicconch","tictactoe"]
_userCmds = ["login", "store", "buygame", "listgame", "searchmygame", "storesearch", "history", "help", "save", "exit","magicconch","tictactoe"]
_valCommand = fb.merge(_adminCmds, _userCmds)


_loggedUser = ["0", "1", "2", "3", "4", 0]
"""Data user yang telah login
0 : id
1 : username
2 : nama
3 : password
4 : role (admin/user)
5 : saldo
"""


_usersData = [["0", "1", "2", "3", "4", 0]]
"""Diimport dari user.csv sebagai variabel global
0 : id
1 : username
2 : nama
3 : password
4 : role (admin/user)
5 : saldo
"""

_gameData = [["0", "1", "2", 2000, 0, 0]]
"""Diimport dari game.csv sebagai variabel global
0 : id
1 : nama
2 : kategori
3 : tahun rilis
4 : harga
5 : stok
"""

_history = [["0", "1", 0, "3", 2000]]
"""Diimport dari riwayat.csv sebagai variabel global
0 : id game
1 : nama game
2 : harga game
3 : id pembeli
4 : tahun pembelian
"""

_possession = [["0", "1"]]
"""Diimport dari kepemilikan.csv sebagai variabel global
0 : id game
1 : id pemilik
"""


def roleCmdIsValid(_role, command, _adminCmds, _userCmds):
    """ validasi command sesuai role """
    _cekCommand = False
    if _role == "admin":
        if fd.find(_adminCmds, command) != -1:
            _cekCommand = True
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')
    else: #_role == "user"
        if fd.find(_userCmds, command) != -1:
            _cekCommand = True
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')

    return _cekCommand


def mintaCommand():
    global _role, _loggedIn, _adminCmds, _userCmds, _valCommand, _loggedUser, _usersData, _gameData, _history, _possession, running
    if _loggedIn:
        os.system("cls") # design
        fb.blit(_loggedUser)
    print('-'*100)
    command = fd.replace(fd.replace(fd.replace(input(">>> ").lower(), ' ', ''), '_', ''), '-', '')     # Toleransi bagi pengguna yang menggunakan (' '), ('_'), atau ('-') sebagai pengutaraan maksud perintah
    print()
    if fd.find(_valCommand, command) != -1:                 # validasi input command
        if _loggedIn:
            if roleCmdIsValid(_role, command, _adminCmds, _userCmds):              # validasi perintah admin dan user
                if command == "register":
                    _usersData = reg.register(_usersData)
                elif command == "login":
                    print('Anda sudah login! Untuk melihat list command, ketik "help".')
                elif command == "addgame":
                    _gameData = ag.addGame(_gameData)
                elif command == "updategame":
                    ug.ubahGame(_gameData)
                elif command == "updatestock":
                    us.ubahStok(_gameData)
                elif command == "store":           # Melihat daftar game yang ada     
                    lg.listing_game(_gameData)
                elif command == "buygame":
                    lg.listing_game(_gameData)
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
                elif command == "storesearch":
                    F11.search_game_at_store(_gameData)
                elif command == "history":
                    history.history(_history, _loggedUser)
                elif command == "topup":
                    _usersData = topup.topup(_usersData)
                elif command == "help":
                    help.help(_role)
                elif command == "exit":
                    running = exit.exit(_usersData, _gameData, _history, _possession, _loggedIn)
                elif command == "save":
                    cari = input("Masukkan nama folder penyimpanan : ")         # Melakukan save
                    print("")
                    print("Saving")
                    sv.simpan(_possession,"kepemilikan",cari)
                    sv.simpan(_gameData,"game",cari)
                    sv.simpan(_usersData,"user",cari)
                    sv.simpan(_history,"riwayat",cari)
                    print("Data telah disimpan pada folder " + cari +"!")
                    
                elif command == "magicconch":
                    mcs.kerangAjaib()                       # Kerang Ajaib
                elif command == "tictactoe" :
                    tt.tictactoe()
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
            elif command == "exit":
                running = exit.exit(_usersData, _gameData, _history, _possession, _loggedIn)                       
            else:
                # validasi perintah, tidak boleh melakukan apa-apa sebelum login KECUALI HELP
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    
    else: #command != _valCommand[i]
        print('Command tidak ada. Untuk melihat list command, ketik "help".')
        
                


running = True



if __name__ == "__main__":   # Inti program
    data = loading.load()
    if data:    # apabila data tidak kosong atau dapat diproses
        _usersData, _gameData, _history, _possession = data
        fb.printWelcome()
        while running:
            mintaCommand()

        print("Selamat menikmati hari anda :(")
